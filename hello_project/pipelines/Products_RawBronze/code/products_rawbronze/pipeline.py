from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from products_rawbronze.config.ConfigStore import *
from products_rawbronze.udfs.UDFs import *
from prophecy.utils import *
from products_rawbronze.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Products_Raw = Products_Raw(spark)
    df_Reformat_Products = Reformat_Products(spark, df_Products_Raw)
    Products_Bronze(spark, df_Reformat_Products)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Products_RawBronze")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Products_RawBronze")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
