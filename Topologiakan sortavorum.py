def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for n in graph[v]:
            if n not in visited:
                dfs(n)
        stack.append(v)

    for v in graph:
        if v not in visited:
            dfs(v)

    return stack[::-1]


dag = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print(topological_sort(dag))
