class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
    def bstInsert(self, root, node):
        if root.left == None and node < root.val:
            root.left = Node(node)

        elif root.right == None and node > root.val:
            root.right = Node(node)

        else:
            if node < root.val:
                self.bstInsert(root.left, node)
            else:
                self.bstInsert(root.right, node)
