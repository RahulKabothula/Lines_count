def read_file(spark, file_path):
    return spark.read.format("text").load(file_path)
