from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from users_bronzesilver.config.ConfigStore import *
from users_bronzesilver.udfs.UDFs import *

def Users_Bronze(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"hello_cicd.{Config.table_name}")
