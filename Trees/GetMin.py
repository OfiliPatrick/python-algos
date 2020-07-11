class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def getMin(self, root):
        if root.left == None:
            return root.val

        return self.getMin(root.left)