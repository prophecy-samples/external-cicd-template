from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from users_bronzesilver.config.ConfigStore import *
from users_bronzesilver.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(
        "start_time",
        expr("lag(ingest_time)").over(Window.partitionBy(col("id")).orderBy(col("ingest_time").asc()))
    )
