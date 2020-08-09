
def allSubSets(arr):
    graph = {}
    graph[0] = arr
    for i in range(len(arr)):
        graph[arr[i]] = arr[i+1:]
    
    sets_so_far = []
    all_subs = []

    def helper(root, sets_so_far):

        if root or root == 0:
            sets_so_far.append(root)
            all_subs.append(sets_so_far[1:])

        children = graph[root]

        for child in children:
            helper(child, sets_so_far)

        sets_so_far.pop()

    helper(0, sets_so_far)

    return all_subs

print(allSubSets([1,2,3]))