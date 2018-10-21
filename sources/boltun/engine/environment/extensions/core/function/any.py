from boltun.engine.environment.extensions import Function


class AnyFunction(Function):

    @classmethod
    def __names__(cls):
        return ['any', 'any_of']

    def __execute__(self, *args):
        return list(args)
