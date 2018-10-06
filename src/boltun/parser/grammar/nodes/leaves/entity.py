from ..__base__ import Filter, Node


class EntityNode(Node):

    def __init__(self, name, filters=None):
        # type: (str, list) -> None
        super(EntityNode, self).__init__()
        self.name = name
        self.filters = filters if filters else []

    def add_filter(self, filter_):
        # type: (Filter) -> None
        self.filters.append(filter_)


class IntentNode(EntityNode):
    pass


class AliasNode(EntityNode):
    pass


class SlotNode(EntityNode):
    pass
