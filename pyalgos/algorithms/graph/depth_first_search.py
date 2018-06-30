import pyalgos.data_structures.graph as g


def noop(x):
    return x


def dfs(graph, vertex, visit=noop, sort=noop):
    stack = [vertex]
    seen = set()
    while stack:
        curr = stack.pop()
        if curr not in seen:
            seen.add(curr)
            visit(curr)
            neighbours = sort(edg.destination for edg in graph.iter_neighbours(curr))
            for vertex in neighbours:
                stack.append(vertex)


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
    dfs(graph, 'a', visit=l.append, sort=sorted)
    assert l == ['a', 'e', 'c', 'g', 'b', 'f', 'd']


if __name__ == '__main__':
    test()
