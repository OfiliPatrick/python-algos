class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, node):
        if root.left == None:
            root.left = Node(node)
            print(root.val)

        else:
            self.insert(root.left, node)
    