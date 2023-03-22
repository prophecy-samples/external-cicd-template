from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from carts_rawbronze.config.ConfigStore import *
from carts_rawbronze.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("id"), 
        col("userId"), 
        col("discountedTotal"), 
        col("totalQuantity"), 
        col("totalProducts"), 
        col("total"), 
        col("product_position"), 
        col("product.discountPercentage").alias("product_discountPercentage"), 
        col("product.discountedPrice").alias("product_discountedPrice"), 
        col("product.id").alias("product_id"), 
        col("product.price").alias("product_price"), 
        col("product.quantity").alias("product_quantity"), 
        col("product.title").alias("product_title"), 
        col("product.total").alias("product_total"), 
        col("ingest_time"), 
        col("env")
    )
