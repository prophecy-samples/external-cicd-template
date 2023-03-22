from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from users_bronzesilver.config.ConfigStore import *
from users_bronzesilver.udfs.UDFs import *

def SchemaTransform_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.withColumnRenamed("ingest_time", "end_time")

    return df1\
        .withColumn("start_time", when(col("start_time").isNull(), to_timestamp(lit("1970-01-01"))).otherwise(col("start_time")))\
        .withColumnRenamed("address.address", "street_address")
