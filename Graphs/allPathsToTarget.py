def allPathsSourceTarget(graph):
    all_paths = []
    path_so_far = []
    target = len(graph) - 1
    root = 0

    def helper(root, path_so_far):
        if root or root >= 0:
            path_so_far.append(root)
            
        if root == target:
            all_paths.append(list(path_so_far))

        children = graph[root]
        for child in children:
            helper(child, path_so_far)

        # if path_so_far:
        path_so_far.pop()

    helper(root,path_so_far)
    
    return all_paths
    
test = [[1, 2], [3], [3], []]

print(allPathsSourceTarget(test))

 
        