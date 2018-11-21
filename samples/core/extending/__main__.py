from boltun.engine import Engine
from boltun.engine.environment.extension import Extension
from boltun.engine.environment.mapping import FunctionDef


class CustomExtension(Extension):

    def __boltun_name__(self):
        return 'custom'

    def __boltun_function_definitions__(self):
        return [
            FunctionDef(name='custom', callable=self.custom_func)
        ]

    # noinspection PyMethodMayBeStatic
    def custom_func(self, value1, value2):
        return str(value1) + " -+- " + str(value2)


if __name__ == '__main__':
    engine = Engine()
    engine.environment.add_extension(CustomExtension())
    result = engine.render(
        "[% custom('Hello', 1) %], human, "
        "{{ how are you ? || you are awesome ! }}"
    )

    for x in list(map(lambda s: str(s), result)):
        print(x)

    # Prints:
    # Hello -+- 1, human, how are you ?
    # Hello -+- 1, human, you are awesome !
