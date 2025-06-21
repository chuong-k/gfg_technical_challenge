import os
import sys
sys.path.append('/opt/spark/work-dir/gfg_technical_challenge/')
from pathlib import Path

from pyspark.sql import DataFrame
import pyspark.sql.functions as F
from pyspark.sql.session import SparkSession

from etl.utils.config_loader import ConfigLoader
from etl.utils.spark_utils import init_spark


# Can be replaced with a ledger module in future
SCHEMA_PATH = '/opt/spark/work-dir/gfg_technical_challenge/etl/config/schema/data_schema.json'
FILE_TYPE = 'json'

# Init config_loader
config_loader = ConfigLoader(SCHEMA_PATH)


def check_directories_exist() -> bool:
    """
    Check to make sure directories exist.
    """
    archive_full_dir = config_loader.load_archive_full_dir()
    raw_full_dir = config_loader.load_raw_full_dir()

    if not Path(archive_full_dir).exists():
        print('[ERROR] {} not exist.\nExiting...'.format(archive_full_dir))
        return False
    if not Path(raw_full_dir).exists():
        print('[ERROR] {} not exist.\nExiting...'.format(raw_full_dir))
        return False
    return True


def read_data(spark: SparkSession) -> DataFrame:
    """
    Load data to spark using schema
    """
    schema = config_loader.load_schema()
    raw_full_dir = config_loader.load_raw_full_dir()

    if FILE_TYPE=='json':
        df = spark.read.schema(schema).json(raw_full_dir)
    else:
        raise NotImplementedError('File type {} not supported yet.'.format(FILE_TYPE))
    return df


def transform(spark: SparkSession,
              df: DataFrame) -> DataFrame:
    df_transormed = (
        df
            .withColumn('used_cc_payment', F.when(F.col('cc_payments') == 1, True).otherwise(False))
            .withColumn('used_paypal_payment', F.when(F.col('paypal_payments') == 1, True).otherwise(False))
            .withColumn('used_afterpay_payment', F.when(F.col('afterpay_payments') == 1, True).otherwise(False))
            .withColumn('used_apple_payment', F.when(F.col('apple_payments') == 1, True).otherwise(False))
    )
    return df_transormed

def main():
    if not check_directories_exist():
        return

    spark = init_spark(app_name="GFG_ETL")
    df = read_data(spark=spark)
    df_transformed = transform(spark, df)

    output_path = "/opt/spark/work-dir/gfg_technical_challenge/data/output/"
    df_transformed.coalesce(1) \
        .write \
        .mode("overwrite") \
        .parquet(output_path)

    print(f"[INFO] Data written to {output_path}")


if __name__ == '__main__':
    main()