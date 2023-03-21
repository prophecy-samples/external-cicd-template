from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from products_rawbronze.config.ConfigStore import *
from products_rawbronze.udfs.UDFs import *

def Reformat_Products(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("brand"), 
        col("category"), 
        col("description"), 
        col("discountPercentage"), 
        col("id").cast(LongType()).alias("id"), 
        col("images"), 
        col("price").cast(FloatType()).alias("price"), 
        col("rating").cast(FloatType()).alias("rating"), 
        col("stock").cast(LongType()).alias("stock"), 
        col("thumbnail"), 
        col("title"), 
        col("ingest_time"), 
        lit("").alias("env")
    )
