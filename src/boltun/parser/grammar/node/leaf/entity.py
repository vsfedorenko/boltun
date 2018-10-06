from ..__base__ import Filter, Node


class EntityNode(Node):

    def __init__(self, name, ref_names=None, optional=False, filters=None):
        # type: (str, list, bool, list) -> None
        super(EntityNode, self).__init__()
        self.name = name
        self.ref_names = ref_names if ref_names else []
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
