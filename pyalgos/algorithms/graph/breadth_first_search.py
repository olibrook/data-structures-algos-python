def noop(x):
    return x


def bfs(graph, vertex, visit=noop, sort=noop):
    queue = [vertex]
    seen = set()
    while queue:
        curr = queue.pop(0)
        visit(curr)
        neighbours = sort(edg.destination for edg in graph.iter_neighbours(curr))
        for vertex in neighbours:
            if vertex not in seen:
                queue.append(vertex)
                seen.add(vertex)
