from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from products_rawbronze.config.ConfigStore import *
from products_rawbronze.udfs.UDFs import *

def Products_Bronze(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", f"dbfs:/FileStore/Prophecy/hello_cicd/{Config.env}/bronze/products")\
        .mode("overwrite")\
        .saveAsTable(f"hello_cicd.{Config.table_name}")
