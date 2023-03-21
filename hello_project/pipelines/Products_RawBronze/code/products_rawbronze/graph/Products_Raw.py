from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from products_rawbronze.config.ConfigStore import *
from products_rawbronze.udfs.UDFs import *

def Products_Raw(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .schema(
          StructType([
            StructField("brand", StringType(), True), StructField("category", StringType(), True), StructField("description", StringType(), True), StructField("discountPercentage", StringType(), True), StructField("id", StringType(), True), StructField("images", ArrayType(StringType(), True), True), StructField("price", StringType(), True), StructField("rating", StringType(), True), StructField("stock", StringType(), True), StructField("thumbnail", StringType(), True), StructField("title", StringType(), True), StructField("ts", TimestampType(), False)
        ])
        )\
        .load("dbfs:/FileStore/Prophecy/hello_cicd/raw/products.json")
