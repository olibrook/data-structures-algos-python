import pyalgos.data_structures.graph as g
import pyalgos.algorithms.graph.depth_first_search as d


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
    d.dfs(graph, 'a', visit=l.append, sort=sorted)
    assert l == ['a', 'e', 'c', 'g', 'b', 'f', 'd']
