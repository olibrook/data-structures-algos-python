import pyalgos.data_structures.graph as g
import pyalgos.algorithms.graph.shortest_path as sp


def test():
    graph = g.Graph(is_directed=True)
    graph.add_edge('a', 'b')
    graph.add_edge('b', 'c')
    graph.add_edge('c', 'd')
    graph.add_edge('d', 'e')
    graph.add_edge('e', 'f')
    graph.add_edge('a', 'f')

    assert sp.find(graph, 'a', 'e') == ['a', 'b', 'c', 'd', 'e']
    assert sp.find(graph, 'a', 'f') == ['a', 'f']
    assert sp.find(graph, 'e', 'a') is None
