import data_structures.graph as g


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


def test():
    graph = g.Graph(is_directed=True)
    graph.add_edge('a', 'b')
    graph.add_edge('a', 'c')
    graph.add_edge('a', 'e')
    graph.add_edge('b', 'd')
    graph.add_edge('b', 'f')
    graph.add_edge('c', 'g')
    graph.add_edge('f', 'e')
    l = []
    bfs(graph, 'a', visit=l.append, sort=sorted)
    assert l == ['a', 'b', 'c', 'e', 'd', 'f', 'g']


if __name__ == '__main__':
    test()
    print('ok')
