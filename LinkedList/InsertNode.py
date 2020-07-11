class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(self, node, newNode):
    node_after = node.next
    node.next, newNode.next = newNode, node_after