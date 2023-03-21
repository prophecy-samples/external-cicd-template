from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from users_rawbronze.config.ConfigStore import *
from users_rawbronze.udfs.UDFs import *

def Users_Reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("address"), 
        col("age").cast(IntegerType()).alias("age"), 
        col("bank"), 
        to_date(col("birthDate")).alias("birthDate"), 
        col("bloodGroup"), 
        col("company"), 
        col("domain"), 
        col("ein"), 
        col("email"), 
        col("eyeColor"), 
        col("firstName"), 
        col("gender"), 
        col("hair"), 
        col("height").cast(FloatType()).alias("height"), 
        col("id").cast(LongType()).alias("id"), 
        col("image"), 
        col("ip"), 
        col("lastName"), 
        col("macAddress"), 
        col("maidenName"), 
        col("password"), 
        col("phone"), 
        col("ssn"), 
        col("university"), 
        col("userAgent"), 
        col("username"), 
        col("weight").cast(DoubleType()).alias("weight"), 
        col("ts")
    )
