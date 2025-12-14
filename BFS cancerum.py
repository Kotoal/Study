def bfs_shortest(graph, start):
    dist = {start: 0}
    queue = [start]

    while queue:
        v = queue.pop(0)
        for n in graph[v]:
            if n not in dist:
                dist[n] = dist[v] + 1
                queue.append(n)
    return dist


graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

print(bfs_shortest(graph, 1))