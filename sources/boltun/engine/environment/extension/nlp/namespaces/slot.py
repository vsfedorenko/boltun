from boltun.engine.environment.extension import Namespace


class SlotNamespace(Namespace):

    @classmethod
    def __boltun_name__(cls):
        return ['slot']
