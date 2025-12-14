def jarvis(points):
    hull = []
    left = min(points)
    p = left

    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            if q == p or (r[0]-p[0])*(q[1]-p[1]) > (r[1]-p[1])*(q[0]-p[0]):
                q = r
        p = q
        if p == left:
            break
    return hull


print(jarvis([(0,0),(1,1),(2,2),(0,2),(2,0)]))
