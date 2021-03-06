def noop(x):
    return x


def bfs(graph, vertex, visit=noop):
    queue = [vertex]
    seen = set()
    while queue:
        curr = queue.pop(0)
        visit(curr)
        for vertex in graph.vertices_from(curr):
            if vertex not in seen:
                queue.append(vertex)
                seen.add(vertex)
