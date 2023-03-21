from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, env: str=None):
        self.spark = None
        self.update(env)

    def update(self, env: str="unspecified"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.env = env
        pass
