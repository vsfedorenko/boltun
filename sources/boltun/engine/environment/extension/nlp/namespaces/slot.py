from boltun.engine.environment.extension import Namespace


class SlotNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['slot']
