from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from users_rawbronze.config.ConfigStore import *
from users_rawbronze.udfs.UDFs import *

def Users_Bronze(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", f"dbfs:/FileStore/Prophecy/hello_cicd/{Config.env}/bronze/users")\
        .mode("append")\
        .saveAsTable(f"hello_cicd.{f"{Config.env}_Users_Bronze"}")
