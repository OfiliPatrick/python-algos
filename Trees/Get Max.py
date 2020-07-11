class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def getMax(self, root):
        if root.right == None:
            return root.val
        return self.getMax(root.right)