class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def preOrd(self, root):
        li = []
        def helper(root):
            if root:
                print(root.val)
                li.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return li

    def inOrd(self, root):
        li = []
        def helper(root):
            if root:
                helper(root.left)
                li.append(root.val)
                helper(root.right)
        helper(root)
        return li

    def postOrd(self, root):
        li = []
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                li.append(root.val)
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

    def bstSearch(self, root, key):
        if root == None:
            return False

        elif root.val == key:
            return True

        else:
            if key < root.val:
                return self.binTreeSearch(root.left, key)
                
            else:
                return self.binTreeSearch(root.right, key)

    def insert(self, root, node):
        if root.left == None:
            root.left = Node(node)
            print(root.val)

        else:
            self.insert(root.left, node)
    
    def bstInsert(self, root, node):
        if root.left == None and node < root.val:
            root.left = Node(node)

        elif root.right == None and node > root.val:
            root.right = Node(node)

        else:
            if node < root.val:
                self.bstInsert(root.left, node)
            else:
                self.bstInsert(root.right, node)

    def treeDelete(self, root, node):
        pass

    def getMin(self, root):
        if root.left == None:
            return root.val

        return self.getMin(root.left)

    def getMax(self, root):
        if root.right == None:
            return root.val
        return self.getMax(root.right)
        
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


    def invertTree(self, root):
        def helper(root):
            if root == None:
                return None  
            left = helper(root.left)
            right = helper(root.right)
            root.left, root.right = root.right , root.left
        helper(root)
        return root


#      8
#    /   \
#   3    10
#  / \     \
# 1   6    14

# tree = Node(8)               
# tree.left = Node(3)
# tree.right = Node(10)
# tree.left.left = Node(1)
# tree.left.right = Node(6)
# tree.right.right = Node(14)

tree = Node(4)               
tree.left = Node(2)
tree.right = Node(7)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right.left = Node(6)
tree.right.right = Node(9)


# arr = [8, 5,2,3, 10, 1, 6, 14]
# print(tree.bstFromArray(arr))

ans = tree.invertTree(tree)
print(tree.levelOrd(ans))
# print(tree)



