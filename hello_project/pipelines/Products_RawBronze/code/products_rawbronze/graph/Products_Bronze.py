from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from products_rawbronze.config.ConfigStore import *
from products_rawbronze.udfs.UDFs import *

def Products_Bronze(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", "dbfs:/FileStore/Prophecy/hello_cicd/bronze/products")\
        .mode("append")\
        .saveAsTable(f"hello_cicd.products_bronze")
