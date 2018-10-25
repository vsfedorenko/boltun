import inspect


def get_class_by_method(method):
    for cls in inspect.getmro(method.im_class):
        if method.__name__ in cls.__dict__:
            return cls
    return None
