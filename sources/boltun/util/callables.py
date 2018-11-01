import inspect
from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass


@attr.s
class RecursionProcessor(with_metaclass(ABCMeta, object)):

    @abstract_method
    def test(self, value):
        raise NotImplementedError()

    @abstract_method
    def apply(self, callable_instance, value, *args, **kwargs):
        raise NotImplementedError()


@attr.s
class ListRecursionProcessor(RecursionProcessor):

    def test(self, value):
        return isinstance(value, (list,))

    def apply(self, callable_instance_wrapper, value, *args, **kwargs):
        return [
            callable_instance_wrapper(v, *args, **kwargs)
            for v in value
        ]


@attr.s
class DictRecursiveProcessor(RecursionProcessor):

    def test(self, value):
        return isinstance(value, (dict,))

    def apply(self, callable_instance_wrapper, value, *args, **kwargs):
        return {
            k: callable_instance_wrapper(v, *args, **kwargs)
            for k, v in six.iteritems(value)
        }


def recursive(method_or_func=None, value_pos=0, value_key=None,
              recursive_iters=None):
    if recursive_iters is None:
        recursive_iters = [
            ListRecursionProcessor(),
            DictRecursiveProcessor()
        ]

    def recursive_callable_decorator(callable_instance):
        if not callable(callable_instance):
            raise ValueError(
                "Recursive annotation must be used within a callable")

        arg_spec = inspect.getargspec(callable_instance)

        arg_index = arg_spec.args.index(value_key) \
            if value_key else value_pos

        arg_key = None
        while not arg_key:
            arg_key = value_key if value_key else arg_spec.args[arg_index]

            if arg_key != 'self' and arg_key != 'cls':
                break

            arg_index += 1

        def _get_arg_value(args, kwargs):
            try:
                return args[arg_index]
            except IndexError:
                return kwargs[arg_key]

        def _real_args_kwargs(value, *args, **kwargs):
            merged_args = list()

            left_args_part = args[:arg_index]
            if left_args_part:
                merged_args.extend(left_args_part)

            if arg_key in kwargs:
                kwargs[arg_key] = value
            else:
                merged_args.append(value)

            right_args_part = args[arg_index + 1:]
            if right_args_part:
                merged_args.extend(right_args_part)

            args = merged_args

            return args, kwargs

        def _fake_args_wrapper(func):
            def wrapper(value, *args, **kwargs):
                args, kwargs = _real_args_kwargs(value, *args, **kwargs)
                return func(*args, **kwargs)

            return wrapper

        def wrapper(*args, **kwargs):
            value = _get_arg_value(args, kwargs)

            for recursive_iter in recursive_iters:
                if not recursive_iter.test(value):
                    continue

                fake_wrapper = _fake_args_wrapper(wrapper)
                value = recursive_iter.apply(
                    fake_wrapper, value, *args, **kwargs)
                return value

            fake_callable_instance = _fake_args_wrapper(callable_instance)
            return fake_callable_instance(value, *args, **kwargs)

        return wrapper

    return recursive_callable_decorator(method_or_func) \
        if callable(method_or_func) else recursive_callable_decorator
