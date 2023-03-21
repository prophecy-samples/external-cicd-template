from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from products_rawbronze.graph.Reformat_Products import *
import products_rawbronze.config.ConfigStore as ConfigStore


class Reformat_ProductsTest(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/products_rawbronze/graph/Reformat_Products/in0/schema.json',
            'test/resources/data/products_rawbronze/graph/Reformat_Products/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/products_rawbronze/graph/Reformat_Products/out/schema.json',
            'test/resources/data/products_rawbronze/graph/Reformat_Products/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Reformat_Products(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "brand",
              "category",
              "description",
              "discountPercentage",
              "id",
              "images",
              "price",
              "rating",
              "stock",
              "thumbnail",
              "title"
            ),
            dfOutComputed.select(
              "brand",
              "category",
              "description",
              "discountPercentage",
              "id",
              "images",
              "price",
              "rating",
              "stock",
              "thumbnail",
              "title"
            ),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        ConfigStore.Utils.initializeFromArgs(
            self.spark,
            Namespace(file = f"configs/resources/config/{fabricName}.json", config = None, overrideJson = None)
        )
