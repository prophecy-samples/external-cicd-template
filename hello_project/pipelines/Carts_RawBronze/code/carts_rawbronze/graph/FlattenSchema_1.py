from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carts_rawbronze.config.ConfigStore import *
from carts_rawbronze.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    flt_col = in0.columns
    selectCols = [col("id") if "id" in flt_col else col("id"),  col("userId") if "userId" in flt_col else col("userId"),                   col("discountedTotal") if "discountedTotal" in flt_col else col("discountedTotal"),                   col("totalQuantity") if "totalQuantity" in flt_col else col("totalQuantity"),                   col("totalProducts") if "totalProducts" in flt_col else col("totalProducts"),                   col("total") if "total" in flt_col else col("total"),                   col("product_position") if "product_position" in flt_col else col("product_position"),                   col("product_discountPercentage") if "product_discountPercentage" in flt_col else col("product.discountPercentage")\
                    .alias("product_discountPercentage"),                   col("product_discountedPrice") if "product_discountedPrice" in flt_col else col("product.discountedPrice")\
                    .alias("product_discountedPrice"),                   col("product_id") if "product_id" in flt_col else col("product.id").alias("product_id"),                   col("product_price") if "product_price" in flt_col else col("product.price").alias("product_price"),                   col("product_quantity") if "product_quantity" in flt_col else col("product.quantity")\
                    .alias("product_quantity"),                   col("product_title") if "product_title" in flt_col else col("product.title").alias("product_title"),                   col("product_total") if "product_total" in flt_col else col("product.total").alias("product_total"),                   col("ingest_time") if "ingest_time" in flt_col else col("ingest_time"),                   col("env") if "env" in flt_col else col("env")]

    return in0.select(*selectCols)
