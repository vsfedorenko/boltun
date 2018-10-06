from ..__base__ import Node


class ForkNode(Node):

    def __init__(self):
        super(ForkNode, self).__init__()
        self.children = []

    def add_child(self, node):
        self.children.append(node)
