class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import collections
def findMode(root):
    val_freq = collections.defaultdict(int)
    modes = []

    def preOrderSearch(root):
        if root:
            val_freq[root.val] += 1
            preOrderSearch(root.left)
            preOrderSearch(root.right)

    preOrderSearch(root)
  
    for key in val_freq:
        if val_freq[key] == max(val_freq.values()):
            modes.append(key)

    return modes

root = Node(1)
root.right = Node(2)
root.right.left = Node(1)

print(findMode(root))
        