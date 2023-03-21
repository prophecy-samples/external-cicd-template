from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from carts_rawbronze.config.ConfigStore import *
from carts_rawbronze.udfs.UDFs import *

def Carts_Bronze(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", "dbfs:/FileStore/Prophecy/hello_cicd/bronze/carts")\
        .mode("append")\
        .saveAsTable(f"hello_cicd.Carts_Bronze")
