import attr
import six


@attr.s
class Entity(object):
    name = attr.ib(type=six.string_types)


@attr.s
class Intent(Entity):
    pass


@attr.s
class Alias(Entity):
    pass


@attr.s
class Slot(Entity):
    pass
