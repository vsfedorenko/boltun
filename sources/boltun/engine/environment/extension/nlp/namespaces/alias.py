from boltun.engine.environment.extension import Namespace


class AliasNamespace(Namespace):

    @classmethod
    def __boltun_name__(cls):
        return ['alias']
