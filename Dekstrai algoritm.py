import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for n, w in graph[v]:
            if dist[v] + w < dist[n]:
                dist[n] = dist[v] + w
                heapq.heappush(pq, (dist[n], n))
    return dist


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2)],
    'C': []
}

print(dijkstra(graph, 'A'))
