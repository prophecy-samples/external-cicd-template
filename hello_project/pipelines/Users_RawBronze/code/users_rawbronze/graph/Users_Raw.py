from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from users_rawbronze.config.ConfigStore import *
from users_rawbronze.udfs.UDFs import *

def Users_Raw(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .schema(
          StructType([
            StructField("address", StructType([
              StructField("city", StringType(), True), StructField("coordinates", StructType([
                StructField("lat", DoubleType(), True), StructField("lng", DoubleType(), True)
              ]), True), StructField("postalCode", StringType(), True), StructField("state", StringType(), True), StructField("street", StringType(), True)
            ]), True), StructField("age", StringType(), True), StructField("bank", StructType([
              StructField("cardExpire", StringType(), True), StructField("cardNumber", StringType(), True), StructField("cardType", StringType(), True), StructField("currency", StringType(), True), StructField("iban", StringType(), True)
            ]), True), StructField("birthDate", StringType(), True), StructField("bloodGroup", StringType(), True), StructField("company", StructType([
              StructField("address", StructType([
                StructField("address", StringType(), True), StructField("city", StringType(), True), StructField("coordinates", StructType([
                  StructField("lat", DoubleType(), True), StructField("lng", DoubleType(), True)
                ]), True), StructField("postalCode", StringType(), True), StructField("state", StringType(), True)
              ]), True), StructField("department", StringType(), True), StructField("name", StringType(), True), StructField("title", StringType(), True)
            ]), True), StructField("domain", StringType(), True), StructField("ein", StringType(), True), StructField("email", StringType(), True), StructField("eyeColor", StringType(), True), StructField("firstName", StringType(), True), StructField("gender", StringType(), True), StructField("hair", StructType([
              StructField("color", StringType(), True), StructField("type", StringType(), True)
            ]), True), StructField("height", StringType(), True), StructField("id", StringType(), True), StructField("image", StringType(), True), StructField("ip", StringType(), True), StructField("lastName", StringType(), True), StructField("macAddress", StringType(), True), StructField("maidenName", StringType(), True), StructField("password", StringType(), True), StructField("phone", StringType(), True), StructField("ssn", StringType(), True), StructField("university", StringType(), True), StructField("userAgent", StringType(), True), StructField("username", StringType(), True), StructField("weight", StringType(), True), StructField("ingest_time", TimestampType(), False)
        ])
        )\
        .load("dbfs:/FileStore/Prophecy/hello_cicd/raw/users.json")
