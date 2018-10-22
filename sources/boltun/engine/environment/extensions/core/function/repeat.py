from boltun.engine.environment.extensions import Function


class RepeatFunction(Function):
    @classmethod
    def __names__(cls):
        return ['repeat']

    def __execute__(self, subject, count=2):
        if isinstance(count, list):
            return [
                RepeatFunction.__repeat(subject, current_count)
                for current_count in count
            ]

        return RepeatFunction.__repeat(subject, count)

    @staticmethod
    def __repeat(subject, count):
        return "".join([subject for _ in range(0, count)])
