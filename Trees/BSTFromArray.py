class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def bstFromArray(self,arr):
        root = Node(arr[0])
        def helper(root ,num):
            if root.left == None and num < root.val:
                root.left = Node(num)
            elif root.right == None and num > root.val:
                root.right = Node(num)
            else:
                if num < root.val:
                    helper(root.left, num)
                else:
                    helper(root.right, num)
        for i in range(1,len(arr)):
            helper(root, arr[i])   
        return self.inOrd(root)
