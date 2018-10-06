class Node(object):

    def __init__(self):
        super(Node, self).__init__()
        self._children = []

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Filter(object):

    def __init__(self, name, args=None, kwargs=None):
        # type: (str, list, dict) -> None
        super(Filter, self).__init__()
        self.name = name
        self.args = args if args else []
        self.kwargs = kwargs if kwargs else {}

    def __repr__(self):
        # type: () -> str
        return "%s(%r)" % (self.__class__, self.__dict__)
