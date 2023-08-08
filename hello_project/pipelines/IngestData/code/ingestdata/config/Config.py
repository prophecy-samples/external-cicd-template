from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, env: str=None, **kwargs):
        self.spark = None
        self.update(env)

    def update(self, env: str="unspecified", **kwargs):
        prophecy_spark = self.spark
        self.env = env
        pass
