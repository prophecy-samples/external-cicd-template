from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from products_rawbronze.graph.Reformat_Products import *
from products_rawbronze.config.ConfigStore import *


class Reformat_ProductsTest(BaseTestCase):

    def test_date_checking(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/products_rawbronze/graph/Reformat_Products/in0/schema.json',
            'test/resources/data/products_rawbronze/graph/Reformat_Products/in0/data/test_date_checking.json',
            'in0'
        )
        dfOutComputed = Reformat_Products(self.spark, dfIn0)
        assertPredicates("out", dfOutComputed, list(zip([(current_timestamp() > col("ingest_time"))], ["date sanity"])))

    def test_deliberatepassfailtest(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/products_rawbronze/graph/Reformat_Products/in0/schema.json',
            'test/resources/data/products_rawbronze/graph/Reformat_Products/in0/data/test_deliberatepassfailtest.json',
            'in0'
        )
        dfOutComputed = Reformat_Products(self.spark, dfIn0)
        assertPredicates("out", dfOutComputed, list(zip([lit(True)], ["deliberately pass or fail "])))

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
