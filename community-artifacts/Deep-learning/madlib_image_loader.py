#!/usr/bin/env python
#
# Python module to load images into postgres or greenplum db, for
#  use with madlib deep_learning module.
#
# The format of the image tables created will have at least 3 columns:
#     (id SERIAL, x REAL[], y).  Each row is 1 image,
#     with image data represented by x (a 3D array of type "real"), and
#     y (category) as text.  id is just a unique identifier for each image,
#     so they don't get mixed up during prediction.  If images are being
#     loaded from disk, there will be an additional img_name column containing
#     the filename of the image, to help identify later.
#
#   ImageLoader.ROWS_PER_FILE = 1000 by default; this is the number of rows per
#      temporary file (or StringIO buffer) loaded at once.
#

# There are two ways of using this module.  One is to load it with:
#  import madlib_image_loader
#     (make sure it is in a directory python knows about.
#      Try adding the directory to PYTHONPATH if it can't find it.)
#
# and use the exposed classes and functions described below.
#
# The second way is to run it directly, passing all options on the
#  command line.  The second way only supports loading images
#  from disk, whereas the first way can be used either to do that or
#  to load them from a dataset already in an existing numpy array (such
#  as the datasets that come prepackaged with keras).
#
#   The module API is pretty simple, only involving two classes:
#     ImageLoader
#     DbCredentials
#
#     two functions (in addition to the class constructors):
#
#   ImageLoader.load_dataset_from_np
#   ImageLoader.load_dataset_from_disk
#
#     and one adjustable parameter (change if default is not working well):
#
#   ImageLoader.ROWS_PER_FILE=1000
#
#
#   Workflow
#
#     1. Create objects:
#
#           db_creds = DbCredentials(db_name='madlib', user=None, password='',
#                                    host='localhost', port=5432)
#
#           iloader = ImageLoader(db_creds, num_workers, table_name=None)
#
#     2a. Perform parallel image loading from numpy arrays:
#
#           iloader.load_dataset_from_np(data_x, data_y, table_name,
#                                        append=False)
#
#       data_x contains image data in np.array format, and data_y is a 1D np.array
#           of the image categories (labels).
#
#       Default database credentials are: localhost port 5432, madlib db, no
#           password.  Calling the default constructor DbCredentials() will attempt
#           to connect using these credentials, but any of them can be overriden.
#
#       append=False attempts to create a new table, while append=True appends more
#           images to an existing table.
#
#       If the user passes a table_name while creating ImageLoader object, it will
#           be used for all further calls to load_dataset_from_np.  It can be
#           changed by passing it as a parameter during the actual call to
#           load_dataset_from_np, and if so future calls will load to that table
#           name instead.  This avoids needing to pass the table_name again every
#           time, but also allows it to be changed at any time.
#
#  or,
#
#     2b. Perform parallel image loading from disk:
#
#           load_dataset_from_disk(self, root_dir, table_name, num_labels='all',
#               append=False):
#
#       Calling this function instead will look in root_dir on the local disk of
#           wherever this is being run.  It will skip over any files in that
#           directory, but will load images contained in each of its
#           subdirectories.  The images should be organized by category/class,
#           where the name of each subdirectory is the label for the images
#           contained within it.
#
#       The table_name and append parameters are the same as described
#           above.  num_labels is an optional parameter which can be used to
#           restrict the number of labels (image classes) loaded, even if more
#           are found in root_dir.  For example, for a large dataset you may
#           have hundreds of labels, but only wish to use a subset of that
#           containing a few dozen.
#
#
# If you want to load an image dataset from disk, but don't feel like writing
#  any python code to call the API, you can just run this file directly, passing
#  these parameters on the command line.
#
# usage: madlib_image_loader.py [-h] [-r ROOT_DIR] [-n NUM_LABELS] [-d DB_NAME]
#                               [-a] [-w NUM_WORKERS] [-p PORT] [-U USERNAME]
#                               [-t HOST] [-P PASSWORD]
#                               table_name
#
# positional arguments:
#   table_name            Name of table where images should be loaded
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -r ROOT_DIR, --root-dir ROOT_DIR
#                         Root directory of image directories (default: .)
#   -n NUM_LABELS, --num-labels NUM_LABELS
#                         Number of image labels (categories) to load. (default:
#                         all)
#   -d DB_NAME, --db-name DB_NAME
#                         Name of database where images should be loaded
#                         (default: madlib)
#   -a, --append          Name of database where images should be loaded
#                         (default: False)
#   -w NUM_WORKERS, --num-workers NUM_WORKERS
#                         Name of parallel workers. (default: 5)
#   -p PORT, --port PORT  database server port (default: 5432)
#   -U USERNAME, --username USERNAME
#                         database user name (default: None)
#   -t HOST, --host HOST  database server host. (default: localhost)
#   -P PASSWORD, --password PASSWORD
#                         database user password (default: None)
#   -m, --no-temp-files   no temporary files, construct all image tables in-
#                         memory (default: False)
#

import argparse
from cStringIO import StringIO
from multiprocessing import Pool, current_process
import os
import random
import signal
from shutil import rmtree
import string
import time
import traceback

import psycopg2 as db
import numpy as np
from PIL import Image

class SignalException(Exception):
    pass

def _worker_sig_handler(signum, frame):
    if signum == signal.SIGINT:
        msg = "Received SIGINT in worker."
    elif signum == signal.SIGTERM:
        msg = "Received SIGTERM in worker."
        _worker_cleanup(None)
    elif signum == signal.SIGSEGV:
        msg = "Received SIGSEGV in worker."
        traceback.print_stack(frame)
    else:
        msg = "Received unknown signal in worker"

    raise SignalException(msg)

def _call_disk_worker(label):
    global iloader
    iloader.call_disk_worker(label)

def _call_np_worker(data): # data = list of (x, y) or (x, y, num_images) tuples
    try:                   #        of length self.ROWS_PER_FILE
        if iloader.no_temp_files:
            iloader._just_load(data)
        else:
            iloader._write_tmp_file_and_load(data)
    except Exception as e:
        if iloader.tmp_dir:
            iloader.rm_temp_dir()
        # For some reason, when an exception is raised in a worker, the
        #  stack trace doesn't get shown.  So we have to print it ourselves
        #  (actual exception #  msg will get printed by mother process.
        #
        print "\nError in {0} while loading images".format(iloader.pr_name)
        print traceback.format_exc()
        raise e

# dummy param needed so this can be called for
# each worker from Pool.map()
def _worker_cleanup(dummy):
    if iloader.tmp_dir:
        iloader.rm_temp_dir()

def init_worker(mother_pid, table_name, append, no_temp_files, db_creds,
                from_disk, root_dir=None):
    pr = current_process()
    print("Initializing {0} [pid {1}]".format(pr.name, pr.pid))

    try:
        iloader = ImageLoader(db_creds=db_creds)
        iloader.mother_pid = mother_pid
        iloader.table_name = table_name
        iloader.no_temp_files = no_temp_files
        iloader.root_dir = root_dir
        iloader.from_disk = from_disk
        signal.signal(signal.SIGINT, _worker_sig_handler)
        signal.signal(signal.SIGSEGV, _worker_sig_handler)
        if not no_temp_files:
            iloader.mk_temp_dir()
        iloader.db_connect()
    except Exception as e:
        if iloader.tmp_dir:
            iloader.rm_temp_dir()
        print "\nException in {0} init_worker:".format(pr.name)
        print traceback.format_exc()
        raise e

class DbCredentials:
    def __init__(self, db_name='madlib', user=None, password='',
                 host='localhost', port=5432):
        if user:
            self.user = user
        else:
            self.user = os.environ["USER"]

        self.db_name = db_name
        self.password = password
        self.host = host
        self.port = port

class ImageLoader:
    def __init__(self, db_creds=None, num_workers=None, table_name=None):
        self.num_workers = num_workers
        self.append = False
        self.img_num = 0
        self.db_creds = db_creds
        self.db_conn = None
        self.db_cur = None
        self.tmp_dir = None
        self.mother = False
        self.pr_name = current_process().name
        self.table_name = table_name
        self.root_dir = None
        self.pool = None
        self.no_temp_files = False

        global iloader  # Singleton per process
        iloader = self

    def terminate_workers(self):
        if iloader.pool:
            iloader.pool.map(_worker_cleanup, [0] * self.num_workers)

        self.pool.terminate()
        self.pool = None
        print("{} workers terminated.".format(self.num_workers))

    def _random_string(self):
        return ''.join([random.choice(string.ascii_letters + string.digits)\
            for n in xrange(10)])

    def mk_temp_dir(self):
        self.tmp_dir = '/tmp/madlib_{0}'.format(self._random_string())
        os.mkdir(self.tmp_dir)
        print("{0}: Created temporary directory {1}"\
            .format(self.pr_name, self.tmp_dir))

    def rm_temp_dir(self):
        rmtree(self.tmp_dir)
        print("{0}: Removed temporary directory {1}"\
            .format(self.pr_name, self.tmp_dir))
        self.tmp_dir = None

    def db_connect(self):
        if self.db_cur:
            return

        db_name = self.db_creds.db_name
        user = self.db_creds.user
        host = self.db_creds.host
        port = self.db_creds.port
        password = self.db_creds.password
        connection_string = "dbname={0} user={1} host={2} port={3} password={4}"\
                            .format(db_name, user, host, port, password)

        try:
            self.db_conn = db.connect(connection_string)
            self.db_cur = self.db_conn.cursor()
            self.db_conn.autocommit = True

        except db.DatabaseError as error:
            self.db_close()
            print(error)
            raise error

        print("{0}: Connected to {1} db.".
            format(self.pr_name, self.db_creds.db_name))

    def db_exec(self, query, args=None, echo=True):
        if self.db_cur is not None:
            if echo:
                print "Executing: {0}".format(query)
            self.db_cur.execute(query, args)
            if echo:
                print self.db_cur.statusmessage
        else:
            raise RuntimeError("{0}: db_cur is None in db_exec"\
                .format(self.pr_name))

    def db_close(self):
        if self.db_cur is not None:
            self.db_cur.close()
            self.db_cur = None
        if isinstance(self.db_conn, db.extensions.connection):
            self.db_conn.close()
            self.db_conn = None

    def _gen_lines(self, data):
        def f(x):
            x = str(x.tolist())
            return x.replace('[','{').replace(']','}')

        for i, row in enumerate(data):
            if len(row) == 3:
                x, y, image_name = row
                yield '{0}|{1}|{2}\n'.format(f(x), y, image_name)
            elif len(row) == 2:
                x, y = row
                yield '{0}|{1}\n'.format(f(x), y)
            else:
                raise RuntimeError("Cannot write invalid row to table:\n{0}"\
                    .format(row))

    def _write_file(self, file_object, data):
        lines = self._gen_lines(data)
        file_object.writelines(lines)

    # This is default value, can be overriden by user, by setting
    #   iloader.ROWS_PER_FILE after ImageLoader is created.
    ROWS_PER_FILE = 1000

    # Copies from open file-like object f into database
    def _copy_into_db(self, f, data):
        table_name = self.table_name

        if self.from_disk:
            self.db_cur.copy_from(f, table_name, sep='|', columns=['x','y',
                                                                   'img_name'])
        else:
            self.db_cur.copy_from(f, table_name, sep='|', columns=['x','y'])

        print("{0}: Loaded {1} images into {2}".format(self.pr_name, len(data),
                                                       self.table_name))

    # Use in-memory buffer as file-like object to load a block of data into db
    #  (no temp files written)
    def _just_load(self, data):
        f = StringIO()
        self._write_file(f, data)
        self._copy_into_db(f, data)
        f.close()

    # Write out a temporary file and then load it into db as a table
    def _write_tmp_file_and_load(self, data):
        table_name = self.table_name

        if not self.tmp_dir:
            print("{0}: Can't find temporary directory... exiting."\
                .format(self.pr_name))
            time.sleep(1) # allow some time for p.terminate() to be called
            return

        filename = os.path.join(self.tmp_dir, '{0}{1:04}.tmp'.format(
            table_name, self.img_num))

        self.img_num += 1
        with file(filename, 'w') as f:
            self._write_file(f, data)

        print("{0}: Wrote {1} images to {2}".format(self.pr_name, len(data),
            filename))

        with file(filename, 'r') as f:
            self._copy_into_db(f, data)

    def _validate_input_and_create_table(self, data_x=[], data_y=[]):
        if len(data_x) != len(data_y):
            raise ValueError("Invalid dataset passed, number of labels in "
                             "data_y ({0}) does not match number of images "
                             "in data_x ({1})"\
                .format(len(data_y), len(data_x)))

        self.db_connect()

        if self.append:
            # Validate that table already exists
            try:
                self.db_exec("SELECT count(*) FROM {0}".format(self.table_name),
                             echo=False)
            except db.DatabaseError:
                raise RuntimeError("append=True passed, but cannot append to "
                                   "table {0} in db {1}.  Either make sure the "
                                   "table exists and you have access to it, or "
                                   "use append=False (default) to auto-create it"
                                   "during loading."
                    .format(self.table_name, self.db_creds.db_name))

            print "Appending to table {0} in {1} db".format(self.table_name,
                                                            self.db_creds.db_name)
        else:
            # Create new table
            try:
                if self.from_disk:
                    sql = "CREATE TABLE {0} (id SERIAL, x REAL[], y TEXT,\
                        img_name TEXT)".format(self.table_name)
                else:
                    sql = "CREATE TABLE {0} (id SERIAL, x REAL[], y TEXT)"\
                        .format( self.table_name)
                self.db_exec(sql)
            except db.DatabaseError as e:
                raise RuntimeError("{0} while creating {1} in db {2}.\n"
                                   "If the table already exists, you can use "
                                   "append=True to append more images to it."
                                .format(e.message.strip(), self.table_name,
                                        self.db_creds.db_name))

            print "Created table {0} in {1} db".format(self.table_name,
                self.db_creds.db_name)

        self.db_close()

    def load_dataset_from_np(self, data_x, data_y, table_name=None,
                             append=False):
        """
        Loads a numpy array into db.  For append=False, creates a new table and
            loads the data.  For append=True, appends data to existing table.
            Throws an exception if append=False and table_name already exists,
            or if append=True and table_name does not exist.  Makes use of
            worker processes initialized during ImageLoader object creation to
            load in parallel.
        @data_x independent variable data, a numpy array of images.  Size of
            first dimension is number of images.  Rest of dimensions determined
            by image resolution and number of channels.
        @data_y dependent variable data (image classes), as an numpy array
        @table_name Name of table in db to load data into
        @append Whether to create a new table (False) or append to an existing
            one (True).  If unspecified, default is False
        """
        start_time = time.time()
        self.mother = True
        self.from_disk = False
        self.append = append

        if table_name:
            self.table_name = table_name

        if not self.table_name:
            raise ValueError("Must specify table_name either in ImageLoader"
                " constructor or in load_dataset_from_np params!")

        self._validate_input_and_create_table(data_x, data_y)

        data_y = data_y.flatten()
        data = zip(data_x, data_y)

        if not self.pool:
            print("Spawning {0} workers...".format(self.num_workers))
            self.pool = Pool(processes=self.num_workers,
                     initializer=init_worker,
                     initargs=(current_process().pid,
                               self.table_name,
                               self.append,
                               False,
                               self.db_creds,
                               False))


        datas = []

        for n in range(0, len(data), self.ROWS_PER_FILE):
            datas.append(data[n:n+self.ROWS_PER_FILE])

        #
        # Each element in datas is a list of self.ROWS_PER_FILE rows
        #
        #  Shape of datas:  ( number of files, rows per file, ( x-dim, y-dim ) )
        #
        #  ( inside x can also be a numpy tensor with several dimensions, but y
        #    should just be a single scalar )
        #
        #  multiprocessing library will call _call_np_worker() in some worker for
        #   each file, splitting the list of files up into roughly equal chunks
        #   for each worker to handle.  For example, if there are 500 files and
        #   5 workers, each will handle about 100 files, and _call_np_worker()
        #   will be called 100 times, each time with a different file full
        #   of images.

        try:
            self.pool.map(_call_np_worker, datas)
        except(Exception) as e:
            self.terminate_workers()
            raise e

        end_time = time.time()
        print("Done!  Loaded {0} images in {1}s"\
            .format(len(data), end_time - start_time))

        self.terminate_workers()

    def call_disk_worker(self, label):
        dir_name = os.path.join(self.root_dir,label)

        filenames = os.listdir(dir_name)
        data = []
        first_image = Image.open(os.path.join(self.root_dir, label, filenames[0]))
        for index, filename in enumerate(filenames):
            image = Image.open(os.path.join(self.root_dir, label, filename))
            x = np.array(image)
            if x.shape != np.array(first_image).shape:
                raise Exception("Images {0} and {1} in label {2} have different "
                                "shapes {0}:{3} {1}:{4}.  Make sure that all the "
                                "images are of the same shape."\
                    .format(filenames[0], filename, label,
                            first_image.shape, x.shape))

            data.append((x, label, filename))
            if (index % self.ROWS_PER_FILE) == (self.ROWS_PER_FILE - 1):
                _call_np_worker(data)
                data = []

        if len(data) > 0:
            _call_np_worker(data)

    def load_dataset_from_disk(self, root_dir, table_name, num_labels='all',
                               append=False):
        """
        Load images from disk into a greenplum database table. All the images
            should be of the same shape.
        @root_dir: Location of the dir which contains all the labels and their
            associated images. Can be relative or absolute. Each label needs to
            have it's own dir and should contain only images inside it's own dir.
            (Extra files in root dir will be ignored, only diretories matter.)
        @table_name: Name of destination table in db
        @num_labels: Num of labels to process/load into a table. By default all
            the labels are loaded.  @table_name: Name of the database table into
            which images will be loaded.
        @append: If set to true, do not create a new table but append to an
            existing table.
        """
        start_time = time.time()
        self.mother = True
        self.append = append
        self.no_temp_files = False
        self.table_name = table_name
        self.from_disk = True
        self._validate_input_and_create_table()

        self.root_dir = root_dir
        subdirs = os.listdir(root_dir)

        labels = []
        # Prune files from directory listing, only use actual sub-directories
        #  This allows the user to keep a tar.gz file or other extraneous files
        #  in the root directory without causing any problems.
        for subdir in subdirs:
            if os.path.isdir(os.path.join(root_dir,subdir)):
                labels.append(subdir)
            else:
                print("{0} is not a directory, skipping".format(subdir))

        if num_labels == 'all':
            print('number of labels = {}'.format(len(labels)))
            num_labels = len(labels)
            print "Found {0} image labels in {1}".format(num_labels, root_dir)
        else:
            num_labels = int(num_labels)
            labels = labels[:num_labels]
            print "Using first {0} image labels in {1}".format(num_labels,
                                                               root_dir)

        if not self.pool:
            print("Spawning {0} workers...".format(self.num_workers))
            self.pool = Pool(processes=self.num_workers,
                             initializer=init_worker,
                             initargs=(current_process().pid,
                                       self.table_name,
                                       self.append,
                                       self.no_temp_files,
                                       self.db_creds,
                                       self.from_disk,
                                       root_dir))
        try:
            self.pool.map(_call_disk_worker, labels)
        except(Exception) as e:
            self.terminate_workers()
            raise e

        self.pool.map(_worker_cleanup, [0] * self.num_workers)

        end_time = time.time()
        print("Done!  Loaded {0} image categories in {1}s"\
            .format(len(labels), end_time - start_time))

        self.terminate_workers()

def main():
    parser = argparse.ArgumentParser(description='Madlib Image Loader',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-r', '--root-dir', action='store',
                        dest='root_dir', default='.',
                        help='Root directory of image directories')

    parser.add_argument('-n', '--num-labels', action='store',
                        dest='num_labels', default='all',
                        help='Number of image labels (categories) to load.')

    parser.add_argument('-d', '--db-name', action='store',
                        dest='db_name', default='madlib',
                        help='Name of database where images should be loaded')

    parser.add_argument('-a', '--append', action='store_true',
                        dest='append', default=False,
                        help='Name of database where images should be loaded')

    parser.add_argument('-w', '--num-workers', action='store',
                        dest='num_workers', default=5,
                        help='Name of parallel workers.')

    parser.add_argument('-p', '--port', action='store',
                        dest='port', default=5432,
                        help='database server port')

    parser.add_argument('-U', '--username', action='store',
                        dest='username', default=None,
                        help='database user name')

    parser.add_argument('-t', '--host', action='store',
                        dest='host', default='localhost',
                        help='database server host.')

    parser.add_argument('-P', '--password', action='store',
                        dest='password', default=None,
                        help='database user password')

#   This option is not working yet
#    parser.add_argument('-m', '--no-temp-files', action='store_true',
#                        dest='no_temp_files', default=False,
#                        help="no temporary files, construct all image tables "
#                             " in-memory")

    parser.add_argument('table_name',
                        help='Name of table where images should be loaded')

    args = parser.parse_args()

    db_creds = DbCredentials(args.db_name, args.username, args.password,
                             args.host, args.port)

    iloader = ImageLoader(db_creds, int(args.num_workers))

    iloader.load_dataset_from_disk(args.root_dir,
                                   args.table_name,
                                   args.num_labels,
                                   args.append)

if __name__ == '__main__':
    main()
