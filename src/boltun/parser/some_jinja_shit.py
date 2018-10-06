import random
from collections import OrderedDict, deque

import six
from jinja2 import Environment, Template
from jinja2.compiler import CodeGenerator
from jinja2.parser import Parser
from jinja2.visitor import NodeVisitor

intent_map = {
    'hello': [
        'hi',
        'hello',
        'welcome',
        'hi, how are you'
    ],
    'name': [
        'vadim',
        'veronika',
        'nadim',
        'nika',
        'maffin',
        'teshka'
    ]
}


# noinspection PyMethodMayBeStatic
class FunctionVisitor(NodeVisitor):

    def __init__(self, filters_include=None, filters_exclude=None):
        super(FunctionVisitor, self).__init__()
        self.filters_include = filters_include
        self.filters_exclude = filters_exclude
        self.queue = deque()
        self.result = []

    def visit_Const(self, node, *args, **kwargs):
        self.queue.append(node.value)

    def visit_Name(self, node, *args, **kwargs):
        self.queue.append(node.name)

    def visit_Call(self, node, *args, **kwargs):
        self.generic_visit(node, *args, **kwargs)
        if len(self.queue) > 0:
            func_items = list(self.queue)
            func_dict = OrderedDict({'name': func_items[0]})
            if len(func_items) > 1:
                func_dict['args'] = func_items[1:]

            include_filters_result = \
                self._filters_accepts(self.filters_include, func_dict) \
                    if self.filters_include else True

            exclude_filters_result = \
                not self._filters_accepts(self.filters_exclude, func_dict) \
                    if self.filters_exclude else True

            if include_filters_result and exclude_filters_result:
                self.result.append(func_dict)

            self.queue.clear()

    def _filters_accepts(self, filters, func_dict):
        for k, v in six.iteritems(filters):
            if k not in func_dict:
                continue

            if not isinstance(v, list):
                v = [v]

            if func_dict.get(k, None) not in v:
                return False

        return True


def generator(*items):
    current_items = items[0]

    if callable(current_items):
        current_items = current_items()

    if isinstance(current_items, list):
        random.shuffle(current_items)

    for v in current_items:
        forward_generator = generator(*items[1:]) \
            if len(items) > 1 else None

        if forward_generator:
            for forward_item in forward_generator:
                result = [v]

                if isinstance(forward_item, list):
                    result.extend(forward_item)
                else:
                    result.append(forward_item)

                yield result
        else:
            yield v


if __name__ == '__main__':
    env = Environment()

    template_str = "{{ intent('hello') }}, {{ intent('name') }} !"
    parser_result = Parser(env, template_str, None, None).parse()

    nodeVisitor = FunctionVisitor(filters_include={'name': ['intent']})
    nodeVisitor.visit(parser_result)
    node_visitor_result = nodeVisitor.result

    code_generator = CodeGenerator(env, name=None, filename=None)
    code_generator.visit(parser_result)
    code_stream = code_generator.stream.getvalue()
    template_code = compile(code_stream, '<template>', 'exec')

    template = Template.from_code(env, template_code, env.make_globals(None))

    lists = []
    for intent_func in node_visitor_result:
        lists.append(intent_map[intent_func.get('args')[0]])

    gen_items = generator(*lists)

    for value in gen_items:
        iterator = iter(value)
        def intent_gen(*args, **kwargs):
            return next(iterator)

        env.globals['intent'] = intent_gen
        print(template.render())
