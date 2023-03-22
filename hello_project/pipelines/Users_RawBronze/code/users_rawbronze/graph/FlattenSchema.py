from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from users_rawbronze.config.ConfigStore import *
from users_rawbronze.udfs.UDFs import *

def FlattenSchema(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("id"), 
        col("username"), 
        col("firstName"), 
        col("lastName"), 
        col("age"), 
        col("birthDate"), 
        col("bloodGroup"), 
        col("domain"), 
        col("ein"), 
        col("email"), 
        col("eyeColor"), 
        col("gender"), 
        col("height"), 
        col("image"), 
        col("ip"), 
        col("macAddress"), 
        col("maidenName"), 
        col("password"), 
        col("phone"), 
        col("ssn"), 
        col("university"), 
        col("userAgent"), 
        col("weight"), 
        col("address.city").alias("address_city"), 
        col("address.coordinates.lat").alias("address_coordinates_lat"), 
        col("address.coordinates.lng").alias("address_coordinates_lng"), 
        col("address.postalCode").alias("address_postalCode"), 
        col("address.state").alias("address_state"), 
        col("address.street").alias("address_street"), 
        col("bank.cardExpire").alias("bank_cardExpire"), 
        col("bank.cardNumber").alias("bank_cardNumber"), 
        col("bank.cardType").alias("bank_cardType"), 
        col("bank.currency").alias("bank_currency"), 
        col("bank.iban").alias("bank_iban"), 
        col("company.address.address").alias("company_address_street"), 
        col("company.address.city").alias("company_address_city"), 
        col("company.address.coordinates.lat").alias("company_address_coordinates_lat"), 
        col("company.address.coordinates.lng").alias("company_address_coordinates_lng"), 
        col("company.address.postalCode").alias("company_address_postalCode"), 
        col("company.address.state").alias("company_address_state"), 
        col("company.department").alias("company_department"), 
        col("company.name").alias("company_name"), 
        col("company.title").alias("company_title"), 
        col("hair.color").alias("hair_color"), 
        col("hair.type").alias("hair_type"), 
        col("ingest_time"), 
        col("env")
    )
