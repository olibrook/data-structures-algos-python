"""Find the shortest path between start end end vertices
in an unweighted graph.

This is BFS modified so that the queue stores complete paths,
rather than only the next vertex to visit. If we find the target
we return the entire path to it.

"""


def find(graph, start, end):
    queue = [[start]]
    seen = set()
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == end:
            return path
        for vertex in graph.vertices_from(curr):
            if vertex not in seen:
                queue.append(path + [vertex])
                seen.add(vertex)
    return None
