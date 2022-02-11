from pyspark.sql import SparkSession

def get_spark_session():
    spark = SparkSession. \
        builder.\
        master("local"). \
        appName("Counting Lines").\
        getOrCreate()
    return spark
