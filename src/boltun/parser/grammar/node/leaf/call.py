from ..__base__ import Filter, Node


class CallNode(Node):

    def __init__(self, name, optional=False, args=None, kwargs=None,
                 filters=None):
        super(CallNode, self).__init__()
        self.name = name
        self.optional = optional
        self.args = args if args else []
        self.kwargs = kwargs if kwargs else {}
        self.filters = filters if filters else []

    def add_filter(self, filter_):
        # type: (Filter) -> None
        self.filters.append(filter_)
