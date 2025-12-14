def intersect(a, b, c, d):
    def ccw(p, q, r):
        return (r[1]-p[1])*(q[0]-p[0]) > (q[1]-p[1])*(r[0]-p[0])

    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


print(intersect((0,0),(4,4),(0,4),(4,0)))
