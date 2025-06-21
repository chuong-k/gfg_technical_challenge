from pyspark.sql import SparkSession

def init_spark(app_name="SparkApp", master="local[*]", config=None):
    builder = SparkSession.builder.appName(app_name).master(master)

    # Apply additional config if provided
    if config:
        for key, value in config.items():
            builder = builder.config(key, value)

    spark = builder.getOrCreate()
    return spark