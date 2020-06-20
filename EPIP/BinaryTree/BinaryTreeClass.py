class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def inOrd(self, root):
        li = []
        def helper(root):
            if root:
                helper(root.left)
                li.append(root.val)
                helper(root.right)
        helper(root)
        return li

    def levelOrd(self, root):
        import collections
        queue = collections.deque([root])
        seen = collections.defaultdict(bool)
        out = []
        while queue:
            curr_node = queue.popleft()
            seen[curr_node] = seen
            out.append(curr_node.val)
            children = [curr_node.left, curr_node.right]
            for child in children:
                if child:
                    queue.append(child)
                    seen[child] = True
        return out

   
    def height(self, root):
        if root == None:
            return -1
            
        left = self.height( root.left)
        right = self.height(root.right)

        return  max(left, right) + 1




#      8
#    /   \
#   3    10
#  / \     \
# 1   6    14
#   

tree = Node(8)               
tree.left = Node(3)
tree.right = Node(10)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.right.right = Node(14)

# print(tree.levelOrd(tree))
print(tree.height(tree))



