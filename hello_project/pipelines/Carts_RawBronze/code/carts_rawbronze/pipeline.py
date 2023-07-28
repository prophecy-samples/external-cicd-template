from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from carts_rawbronze.config.ConfigStore import *
from carts_rawbronze.udfs.UDFs import *
from prophecy.utils import *
from carts_rawbronze.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Carts_Raw = Carts_Raw(spark)
    df_Carts_Reformat = Carts_Reformat(spark, df_Carts_Raw)
    df_SQLStatement_1 = SQLStatement_1(spark, df_Carts_Reformat)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_SQLStatement_1)
    Carts_Bronze(spark, df_FlattenSchema_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Carts_RawBronze")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Carts_RawBronze", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Carts_RawBronze")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
