from boltun.engine.environment.extension import Namespace


class IoNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['io']
