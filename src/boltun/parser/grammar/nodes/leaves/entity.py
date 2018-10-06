from ..__base__ import Filter, Node


class EntityNode(Node):

    def __init__(self, name, optional=False, filters=None):
        # type: (str, bool, list) -> None
        super(EntityNode, self).__init__()
        self.name = name
        self.optional = optional
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
