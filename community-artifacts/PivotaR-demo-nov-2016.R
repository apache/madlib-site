
library(PivotalR)
cid <- db.connect(dbname = "madlib-pg94", host = "127.0.0.1", madlib = "madlib", port = 5094)

### Kmeans Clustering

# Prepare datasets

dat.matrix <- matrix( c(
    1,14.23,1.71,2.43,15.6,127,2.8,3.06,0.28,2.29,5.64,1.04,3.92,1065,
    2,13.2,1.78,2.14,11.2,1,2.65,2.76,0.26,1.28,4.38,1.05,3.49,1050,
    3,13.16,2.36,2.67,18.6,101,2.8,3.24,0.3,2.81,5.6799,1.03,3.17,1185,
    4,14.37,1.95,2.5,16.8,113,3.85,3.49,0.24,2.18,7.8,0.86,3.45,1480,
    5,13.24,2.59,2.87,21,118,2.8,2.69,0.39,1.82,4.32,1.04,2.93,735,
    6,14.2,1.76,2.45,15.2,112,3.27,3.39,0.34,1.97,6.75,1.05,2.85,1450,
    7,14.39,1.87,2.45,14.6,96,2.5,2.52,0.3,1.98,5.25,1.02,3.58,1290,
    8,14.06,2.15,2.61,17.6,121,2.6,2.51,0.31,1.25,5.05,1.06,3.58,1295,
    9,14.83,1.64,2.17,14,97,2.8,2.98,0.29,1.98,5.2,1.08,2.85,1045,
    10,13.86,1.35,2.27,16,98,2.98,3.15,0.22,1.85,7.2199,1.01,3.55,1045),
    byrow=T, nrow=10)
cols <- c("pid", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10",
    "p11", "p12", "p13")
colnames(dat.matrix) <- cols

cent.r <- matrix(
    c(14.23,1.71,2.43,15.6,127,2.8,3.06,0.28,2.29,5.64,1.04,3.92,1065,
       13.2,1.78,2.14,11.2,1,2.65,2.76,0.26,1.28,4.38,1.05,3.49,1050),
    byrow=T, nrow=2)
colnames(cent.r) <- cols[2:14]

dat <- as.db.data.frame(as.data.frame(dat.matrix), conn.id=cid, verbose=FALSE)
cent <- as.db.data.frame(as.data.frame(cent.r), conn.id=cid, verbose=FALSE)


# kmeans
db.out <- madlib.kmeans(dat, 2, key = 'pid')
print(db.out)

# R equivalent
r.out <- kmeans(dat.matrix,2)
print(r.out)

# Variations
db.out <- madlib.kmeans(dat, 2, key = 'pid', nstart = 2)
print(db.out)

db.out <- madlib.kmeans(dat, cent.r, key= 'pid')
print(db.out)

db.out <- madlib.kmeans(dat, centers = cent, key= 'pid')
print(db.out)




### SVM

# Prepare datasets
data <- db.data.frame("abalone", conn.id = cid, verbose = FALSE)
lk(data,10)

# SVM
fit <- madlib.svm(rings > 7 ~ . - id - sex, data = data, type = "classification")
print(fit)

pred <- predict(fit, newdata = data, id.col = "id")
lk(pred,10)


# Grouping
# "|" can be used at the end of the formula to denote that
#   the fitting is done conditioned on the values of one or more
#   variables. For example, ‘y ~ x + sin(z) | v + w’ will do the
#   fitting each distinct combination of the values of ‘v’ and ‘w’.

fit <- madlib.svm(length ~ height + shell | sex + (rings > 7), data = data, type = "regression")
print(fit)

## use I(.) for expressions
fit <- madlib.svm(rings > 7 ~ height + shell + diameter + I(diameter^2),
                       data = data, type = "classification")
print(fit)


### LDA

# Prepare datasets

library(topicmodels)

data("AssociatedPress", package = "topicmodels")
temp_dat <- AssociatedPress
dat1 <- cbind(temp_dat$i,temp_dat$j,temp_dat$v)
dat1 <- as.data.frame(dat1)
colnames(dat1) <- c("docid", "wordid", "count")
dat2 <- as.data.frame(temp_dat$dimnames[2]$Terms)
dat2 <- cbind(1:nrow(dat2),dat2)
colnames(dat2) <- c("wordid", "word")

termfreq <- "__madlib_pivotalr_lda_tf__"
vocab <- "__madlib_pivotalr_lda_vocab__"
newdata <- "__madlib_pivotalr_lda_data__"

dat1 <- as.db.data.frame(dat1, conn.id=cid, verbose=FALSE, is.temp=TRUE, table.name=termfreq)
dat2 <- as.db.data.frame(dat2, conn.id=cid, verbose=FALSE, is.temp=TRUE, table.name=vocab)

sql <- paste("DROP TABLE IF EXISTS ", newdata, "; CREATE TEMP TABLE ", newdata,
             " AS SELECT docid, array_agg(word) AS words ",
             "FROM (SELECT *, generate_series(1,count::int) FROM ",
             termfreq,  " JOIN ", vocab,
             " USING (wordid)) subq GROUP BY docid;", sep="")
db.q(sql, verbose=FALSE)


dat.r <- AssociatedPress

dat <- db.data.frame(newdata, conn.id=cid, verbose=FALSE, is.temp=TRUE)

# LDA

output.db <- madlib.lda(dat, "docid","words",10,0.1,0.1, 50)
output.r <- LDA(AssociatedPress, k=10,
    control=list(iter=50, alpha=0.1, delta=0.1),
    method="Gibbs")

perplexity.db <- perplexity.lda.madlib(output.db)
print(perplexity.db)

perplexity.r <- perplexity(output.r, newdata=AssociatedPress)
print(perplexity.r)

output.db <- madlib.lda(dat, "docid","words",10,0.1,0.1, 50,nstart=3)

