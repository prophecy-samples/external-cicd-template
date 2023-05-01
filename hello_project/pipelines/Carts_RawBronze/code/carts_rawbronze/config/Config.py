from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, env: str=None, table_name: str=None, **kwargs):
        self.spark = None
        self.update(env, table_name)

    def update(self, env: str="unspecified", table_name: str="", **kwargs):
        prophecy_spark = self.spark
        self.env = env
        self.table_name = table_name
        pass
