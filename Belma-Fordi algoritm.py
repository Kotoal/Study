def bellman_ford(edges, n, start):
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


edges = [(0,1,1),(1,2,-1),(0,2,4)]
print(bellman_ford(edges, 3, 0))
