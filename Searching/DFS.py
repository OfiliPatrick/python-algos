graph = {
    'A': ['B', 'C'],
    'B': ['A','D','E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C','E','A','B']
}

def DFS(graph):
    stack = []
    import collections
    cnt = 0
    seen_node = collections.defaultdict(int)
    start = 'A'
    stack.append(start)
    while stack:
        node = stack.pop()
        print(node)
        adjs = graph[node]
        for adj in adjs:
            if seen_node[adj] < 1:
                stack.append(adj)
                seen_node[adj] += 1                

print(DFS(graph))



