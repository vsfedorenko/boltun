from boltun.engine.environment.extension import Namespace


class AliasNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['alias']
