def noop(x):
    return x


def dfs(graph, vertex, visit=noop):
    stack = [vertex]
    seen = set()
    while stack:
        curr = stack.pop()
        if curr not in seen:
            seen.add(curr)
            visit(curr)
            for vertex in graph.vertices_from(curr):
                stack.append(vertex)
