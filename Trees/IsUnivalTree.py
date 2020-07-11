class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def isUnivalTree(self, root):
        import collections
        seen = set()
        def helper(root):
            if root == None:
                return True            
            seen.add(root.val)
            if len(seen) > 1:
                return False
            left =  helper(root.left)
            right = helper(root.right)  
            if left == False:
                return right
            return left
        return helper(root)