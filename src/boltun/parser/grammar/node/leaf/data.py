from ..__base__ import Node


class DataNode(Node):

    def __init__(self, content):
        super(DataNode, self).__init__()
        self.content = content
