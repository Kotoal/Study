def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


matrix = [
    [0, 3, float('inf')],
    [float('inf'), 0, 1],
    [2, float('inf'), 0]
]

print(floyd_warshall(matrix))