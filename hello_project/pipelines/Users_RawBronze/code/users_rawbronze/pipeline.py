from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from users_rawbronze.config.ConfigStore import *
from users_rawbronze.udfs.UDFs import *
from prophecy.utils import *
from users_rawbronze.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Users_Raw = Users_Raw(spark)
    df_Users_Reformat = Users_Reformat(spark, df_Users_Raw)
    df_FlattenSchema = FlattenSchema(spark, df_Users_Reformat)
    Users_Bronze(spark, df_FlattenSchema)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Users_RawBronze")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Users_RawBronze", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Users_RawBronze")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
