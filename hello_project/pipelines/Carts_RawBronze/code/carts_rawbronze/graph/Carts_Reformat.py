from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from carts_rawbronze.config.ConfigStore import *
from carts_rawbronze.udfs.UDFs import *

def Carts_Reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("discountedTotal").cast(DoubleType()).alias("discountedTotal"), 
        col("id").cast(LongType()).alias("id"), 
        col("products"), 
        col("total").cast(DoubleType()).alias("total"), 
        col("totalProducts").cast(LongType()).alias("totalProducts"), 
        col("totalQuantity").cast(LongType()).alias("totalQuantity"), 
        col("userId").cast(LongType()).alias("userId"), 
        col("ts")
    )
