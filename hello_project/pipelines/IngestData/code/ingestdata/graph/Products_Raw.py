from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ingestdata.config.ConfigStore import *
from ingestdata.udfs.UDFs import *

def Products_Raw(spark: SparkSession, in0: DataFrame):
    in0.write.format("json").mode("overwrite").save("dbfs:/FileStore/Prophecy/hello_cicd/raw/products.json")
