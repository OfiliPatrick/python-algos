class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def treeSearch(self, root, key):
        if root == None:
            return False
        elif root.val == key:
            return True
        else:
            res_left = self.treeSearch(root.left, key)
            res_right = self.treeSearch(root.right, key)
            if res_left == False:
                return res_right
            return res_left