def bfs(graph, start):
    visited = [start]
    queue = [start]
    order = []

    while queue:
        v = queue.pop(0)
        order.append(v)
        for n in graph[v]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return order


graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

print(bfs(graph, 1))