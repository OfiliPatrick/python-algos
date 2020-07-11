class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def invertTree(self, root):
        def helper(root):
            if root == None:
                return None  
            left = helper(root.left)
            right = helper(root.right)
            root.left, root.right = root.right , root.left
        helper(root)
        return root
