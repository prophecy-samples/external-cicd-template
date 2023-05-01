from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingestdata.config.ConfigStore import *
from ingestdata.udfs.UDFs import *
from prophecy.utils import *
from ingestdata.graph import *

def pipeline(spark: SparkSession) -> None:
    df_RestAPIEnrich_1 = RestAPIEnrich_1(spark)
    df_Fetch_Data_user_df, df_Fetch_Data_products_df, df_Fetch_Data_carts_df = Fetch_Data(spark)
    df_Source_1 = Source_1(spark)
    Products_Raw(spark, df_Fetch_Data_products_df)
    Carts_Raw(spark, df_Fetch_Data_carts_df)
    Users_Raw(spark, df_Fetch_Data_user_df)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/IngestData")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/IngestData")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
