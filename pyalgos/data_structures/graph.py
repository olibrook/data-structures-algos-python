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
        matching = list(e for e in self.edges() if e.destination == vertex)
        for e in matching:
            del self.graph[e.source][e.destination]

    def edges_from(self, vertex):
        for destination, weight in self.graph[vertex].items():
            yield Edge(vertex, destination, weight)

    def edges(self):
        for source, edges in self.graph.items():
            for destination, weight in edges.items():
                yield Edge(source, destination, weight)

    def vertices_from(self, vertex):
        for destination, _ in self.graph[vertex].items():
            yield destination

    def vertices(self):
        return self.graph.keys()
