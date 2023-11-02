from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carts_rawbronze.config.ConfigStore import *
from carts_rawbronze.udfs.UDFs import *

def Carts_Bronze(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", f"dbfs:/FileStore/Prophecy/hello_cicd/{Config.env}/bronze/carts")\
        .mode("overwrite")\
        .saveAsTable(f"`hello_cicd`.`{Config.table_name}`")
