class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.myl = []
        
   
    def maxHeight(self, node):
        import collections
        start =  node
        queue  = collections.deque()
        queue.append(start)
        out = []; res  = []
        seen = collections.defaultdict(bool)
        level_store = collections.defaultdict(int)
        level_store[start] = 0
        while queue:
            curr_node = queue.popleft()
            out.append(node.val)
            childeren = [curr_node.left, curr_node.right]
            for child in childeren:
                if child != None and seen[child] == False:
                    queue.append(child)
                    seen[child] = True
                    level_store[child] = level_store[curr_node] + 1
        for keyy in level_store:
            res.append(level_store[keyy])
        return res[-1]

