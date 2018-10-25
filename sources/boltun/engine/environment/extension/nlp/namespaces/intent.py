from boltun.engine.environment.extension import Namespace


class IntentNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['intent']
