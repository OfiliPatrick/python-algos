

    def inOrderSearch(root):
        if root:
            preOrderSearch(root.left)
            val_freq[root.val] += 1
            preOrderSearch(root.right)

    inOrderSearch(root)
  
    for key in val_freq:
        if val_freq[key] == max(val_freq.values()):
            modes.append(key)

    return modes

root = Node(1)