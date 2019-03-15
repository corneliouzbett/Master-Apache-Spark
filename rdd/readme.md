# Resilient Distributed Datasets (RDDs)
spark revolves around the concept of RDD, which is a fault-tolerant collection of elements that can be operated on in parallel.

# Two ways to create RDDs
   1. paralleizing an existing collection in your driver program.
   2. referencing a dataset in an external storage system e.g shared filesystem, HDFS, HBase or any data source offering a Hadoop input format.

# Parallelized Collections
Parallelized collections are created by calling SparkContext’s parallelize method on an existing iterable or collection in your driver program. The elements of the collection are copied to form a distributed dataset that can be operated on in parallel.

        data = [1,2,3,4,5,6,7,8,9,10]
        rddData = sc.paralleize(data)

# External Datasets
PySpark can create distributed datasets from any storage source supported by Hadoop, including your local file system, HDFS, Cassandra, HBase, Amazon S3, etc. Spark supports text files, SequenceFiles, and any other Hadoop InputFormat.
Text file RDDs can be created using SparkContext’s textFile method. This method takes an URI for the file (either a local path on the machine, or a hdfs://, s3a://, etc URI) and reads it as a collection of lines.

        distFile = sc.textFile("data.txt")

