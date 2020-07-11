graph = {
    'A': ['B', 'C'],
    'B': ['A','D','E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C','E','A','B']
}
def bfs(graph):
    import collections
    queue = collections.deque()
    seen_node = collections.defaultdict(int)
    cnt = collections.defaultdict(int)
    start_node = 'A'
    queue.append(start_node)
    while queue:
        node =  queue.popleft()
        adjs = graph[node]
        noOfChildren = len(adjs)
        cnt[node] = noOfChildren
        for adj in adjs:
            if seen_node[adj] < 1:
                queue.append(adj)
                seen_node[adj] +=1
    for node in cnt:
        if cnt[node] == max(cnt.values()):
            return node

print(bfs(graph))


print(input('mhbgbbgfd'))