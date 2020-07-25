class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import collections
def findMode(root):
    

    def inOrderSearch(root):
        if root:
            inOrderSearch(root.left)
            val_freq[root.val] += 1
            inOrderSearch(root.right)

    inOrderSearch(root)
  

    return modes

root = Node(1)
root.right = Node(2)
root.right.left = Node(1)

print(findMode(root))
        