from boltun.engine.environment.extension import Namespace


class IntentNamespace(Namespace):

    @classmethod
    def __boltun_name__(cls):
        return ['intent']
