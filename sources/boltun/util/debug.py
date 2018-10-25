from __future__ import print_function

import time


def timed(callable_instance):
    def wrapper(*args, **kwargs):
        t_1 = time.clock()
        result = callable_instance(args, kwargs)
        t_2 = time.clock()

        print("%f seconds" % (t_2 - t_1))

        return result

    return wrapper
