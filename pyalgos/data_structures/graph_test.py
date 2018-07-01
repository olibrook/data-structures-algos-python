import pyalgos.data_structures.graph as g


def test():
    ug = g.Graph(is_directed=False)
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
        assert list(ug.edges_from('v{}'.format(i))) == [
            g.Edge('v{}'.format(i), '#v{}'.format(i), 1)
        ]
        assert list(ug.edges_from('#v{}'.format(i))) == [
            g.Edge('#v{}'.format(i), 'v{}'.format(i), 1)
        ]

    expected_edges = []
    for i in range(10):
        expected_edges.append(g.Edge('v{}'.format(i), '#v{}'.format(i), 1))
        expected_edges.append(g.Edge('#v{}'.format(i), 'v{}'.format(i), 1))
    assert sorted(list(ug.edges())) == sorted(expected_edges)

    expected_vertices = []
    for i in range(10):
        expected_vertices.append('v{}'.format(i))
        expected_vertices.append('#v{}'.format(i))
    assert sorted(list(ug.vertices())) == sorted(expected_vertices)

    for i in range(10):
        ug.delete_vertex('v{}'.format(i))
        ug.delete_vertex('#v{}'.format(i))
    assert ug.graph == {}
