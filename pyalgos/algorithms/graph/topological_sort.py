"""Topologically sort a directed acyclic graph.

Usage example - determine the running order of tasks with constraints
that some tasks must be complete before others can run.

We use dfs and color nodes on entry/exit from the recursion. Doing so
allows us to detect cycles.

Note that because we are using DFS we visit the farthest nodes first
and build the returned list of vertices in reverse.

Note also that not all nodes may be reachable from an arbitrarily-chosen
start node. For that reason, we run DFS on all the vertices in turn, marking
them as visited as we go.

"""


def topological_sort(graph):
    grey = 'grey'
    black = 'black'
    state = {}
    ret = []

    def dfs(vertex):
        if vertex in state:
            return
        state[vertex] = grey
        for neighbour in graph.vertices_from(vertex):
            color = state.get(neighbour, None)
            if color == grey:
                raise ValueError("The graph is not a DAG - found a cycle.")
            if color == black:
                continue
            dfs(neighbour)
        ret.insert(0, vertex)
        state[vertex] = black

    for v in graph.vertices():
        dfs(v)

    return ret
