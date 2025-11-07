# Installation Guide

Information on initial installation and deployment of MADlib into a database instance.

For detailed installation instructions, please visit the [MADlib Wiki Installation Guide](https://cwiki.apache.org/confluence/display/MADLIB/Installation+Guide).

## Quick Installation

### Prerequisites
- PostgreSQL 11+ or Greenplum Database 5.x/6.x/7.x
- Python 3.x
- Required system libraries

### Installation Steps

1. **Download MADlib**
   ```bash
   wget https://dist.apache.org/repos/dist/release/madlib/2.1.0/apache-madlib-2.1.0-src.tar.gz
   ```

2. **Install MADlib**
   ```bash
   tar -xzf apache-madlib-2.1.0-src.tar.gz
   cd apache-madlib-2.1.0-src
   ./configure
   make
   make install
   ```

3. **Deploy to Database**
   ```sql
   SELECT madlib.install_madlib();
   ```

For complete installation instructions, platform-specific guides, and troubleshooting, please refer to the [official installation documentation](https://cwiki.apache.org/confluence/display/MADLIB/Installation+Guide).