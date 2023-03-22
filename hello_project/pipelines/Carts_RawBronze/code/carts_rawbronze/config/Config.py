from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, env: str=None, table_name: str=None):
        self.spark = None
        self.update(env, table_name)

    def update(self, env: str="unspecified", table_name: str=""):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.env = env
        self.table_name = table_name
        pass
