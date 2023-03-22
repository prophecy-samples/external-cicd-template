from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from carts_rawbronze.config.ConfigStore import *
from carts_rawbronze.udfs.UDFs import *

def Carts_Raw(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .schema(
          StructType([
            StructField("discountedTotal", LongType(), True), StructField("id", LongType(), True), StructField("products", ArrayType(
            StructType([
              StructField("discountPercentage", DoubleType(), True), StructField("discountedPrice", LongType(), True), StructField("id", LongType(), True), StructField("price", DoubleType(), True), StructField("quantity", LongType(), True), StructField("title", StringType(), True), StructField("total", LongType(), True)
          ]), 
            True
          ), True), StructField("total", LongType(), True), StructField("totalProducts", LongType(), True), StructField("totalQuantity", LongType(), True), StructField("userId", LongType(), True), StructField("ingest_time", TimestampType(), False)
        ])
        )\
        .load(f"dbfs:/FileStore/Prophecy/hello_cicd/{Config.env}/raw/carts.json")
