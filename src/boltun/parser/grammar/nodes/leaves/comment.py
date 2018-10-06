from ..__base__ import Node


class CommentNode(Node):

    def __init__(self, content):
        super(CommentNode, self).__init__()
        self.content = content
