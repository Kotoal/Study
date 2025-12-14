def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            order.append(v)
            for n in reversed(graph[v]):
                stack.append(n)
    return order


graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

print(dfs(graph, 1))
