from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from users_bronzesilver.config.ConfigStore import *
from users_bronzesilver.udfs.UDFs import *
from prophecy.utils import *
from users_bronzesilver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Users_Bronze = Users_Bronze(spark)
    df_WindowFunction_1 = WindowFunction_1(spark, df_Users_Bronze)
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_WindowFunction_1)
    Users_Silver(spark, df_SchemaTransform_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Users_BronzeSilver")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Users_BronzeSilver")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
