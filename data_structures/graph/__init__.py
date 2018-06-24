import collections

Edge = collections.namedtuple('Edge', ['source', 'destination', 'weight'])


class Graph:
    """A Graph data structure implemented as an adjacency list. For sparse
    graphs, this saves memory compared to an adjacency matrix.

    """
    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.graph = {}

    def add_edge(self, source, destination, weight=1):
        self.graph.setdefault(source, {})[destination] = weight
        destination = self.graph.setdefault(destination, {})
        if not self.is_directed:
            destination[source] = weight

    def delete_edge(self, source, destination):
        del self.graph[source][destination]
        if not self.is_directed:
            del self.graph[destination][source]

    def add_vertex(self, vertex):
        self.graph.setdefault(vertex, {})

    def delete_vertex(self, vertex):
        # Delete vertex and forward edges
        del self.graph[vertex]
        # Delete backward edges
        matching = list(e for e in self.iter_edges() if e.destination == vertex)
        for e in matching:
            del self.graph[e.source][e.destination]

    def iter_neighbours(self, vertex):
        for destination, weight in self.graph[vertex].items():
            yield Edge(vertex, destination, weight)

    def iter_edges(self):
        for source, edges in self.graph.items():
            for destination, weight in edges.items():
                yield Edge(source, destination, weight)

    def iter_vertices(self):
        return self.graph.keys()


if __name__ == '__main__':
    def test():
        ug = Graph(is_directed=False)
        assert ug.graph == {}
        ug.add_edge('a', 'b', 5)
        assert ug.graph == {
            'a': {'b': 5},
            'b': {'a': 5},
        }
        ug.delete_edge('a', 'b')
        assert ug.graph == {
            'a': {},
            'b': {},
        }
        ug.delete_vertex('a')
        ug.delete_vertex('b')
        assert ug.graph == {}

        ug.add_edge('c', 'd', 10)
        assert ug.graph == {
            'c': {'d': 10},
            'd': {'c': 10},
        }
        ug.delete_vertex('c')
        assert ug.graph == {
            'd': {},
        }
        ug.delete_vertex('d')
        assert ug.graph == {}

        for i in range(10):
            ug.add_edge('v{}'.format(i), '#v{}'.format(i))

        for i in range(10):
            assert list(ug.iter_neighbours('v{}'.format(i))) == [
                Edge('v{}'.format(i), '#v{}'.format(i), 1)
            ]
            assert list(ug.iter_neighbours('#v{}'.format(i))) == [
                Edge('#v{}'.format(i), 'v{}'.format(i), 1)
            ]

        expected_edges = []
        for i in range(10):
            expected_edges.append(Edge('v{}'.format(i), '#v{}'.format(i), 1))
            expected_edges.append(Edge('#v{}'.format(i), 'v{}'.format(i), 1))
        assert sorted(list(ug.iter_edges())) == sorted(expected_edges)

        expected_vertices = []
        for i in range(10):
            expected_vertices.append('v{}'.format(i))
            expected_vertices.append('#v{}'.format(i))
        assert sorted(list(ug.iter_vertices())) == sorted(expected_vertices)

        for i in range(10):
            ug.delete_vertex('v{}'.format(i))
            ug.delete_vertex('#v{}'.format(i))
        assert ug.graph == {}

        print('ok')
    test()
