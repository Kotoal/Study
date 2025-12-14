def connected_components(graph):
    visited = set()
    components = []

    def dfs(v, comp):
        visited.add(v)
        comp.append(v)
        for n in graph[v]:
            if n not in visited:
                dfs(n, comp)

    for v in graph:
        if v not in visited:
            comp = []
            dfs(v, comp)
            components.append(comp)

    return components


graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}

print(connected_components(graph))
