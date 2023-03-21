from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from ingestdata.config.ConfigStore import *
from ingestdata.udfs.UDFs import *

def Fetch_Data(spark: SparkSession) -> (DataFrame, DataFrame, DataFrame):
    import requests
    from pyspark.sql.functions import current_timestamp
    user_data = requests.get("https://dummyjson.com/users?limit=1000").json()["users"]

    for u in user_data:
        for (k, v) in u.items():
            if not isinstance(v, dict) and not isinstance(v, list):
                u[k] = str(v)

    user_df = spark.read\
                  .json(spark.sparkContext.parallelize(user_data), samplingRatio = 1.0)\
                  .withColumn("ingest_time", current_timestamp())
    product_data = requests.get("https://dummyjson.com/products?limit=1000").json()["products"]

    for p in product_data:
        for (k, v) in p.items():
            if not isinstance(v, dict) and not isinstance(v, list):
                p[k] = str(v)

    products_df = spark.read\
                      .json(spark.sparkContext.parallelize(product_data), samplingRatio = 1.0)\
                      .withColumn("ingest_time", current_timestamp())
    carts_data = requests.get("https://dummyjson.com/carts?limit=1000").json()["carts"]

    for c in carts_data:
        for p in c["products"]:
            p["price"] = float(p["price"])
            p["discountPercentage"] = float(p["discountPercentage"])

    carts_df = spark.read\
                   .json(spark.sparkContext.parallelize(carts_data), samplingRatio = 1.0)\
                   .withColumn("ingest_time", current_timestamp())

    return (user_df, products_df, carts_df)
