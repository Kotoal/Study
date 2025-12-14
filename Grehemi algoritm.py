def graham(points):
    start = min(points)
    points.remove(start)

    def angle(p):
        return (p[0]-start[0], p[1]-start[1])

    points.sort(key=angle)
    stack = [start, points[0]]

    for p in points[1:]:
        while len(stack) >= 2:
            b = stack.pop()
            a = stack[-1]
            if (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0]) > 0:
                stack.append(b)
                break
        stack.append(p)
    return stack


print(graham([(0,0),(1,1),(2,2),(0,2),(2,0)]))