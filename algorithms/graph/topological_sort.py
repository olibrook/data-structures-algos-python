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
import data_structures.graph as g


def topological_sort(graph, sort=None):
    # Sorting is not part of the algorithm, but gives
    # consistent order for testing.
    sort = sort or (lambda x: x)
    grey = 'grey'
    black = 'black'
    state = {}
    ret = []

    def dfs(vertex):
        if vertex in state:
            return
        state[vertex] = grey
        for edge in sort(graph.iter_neighbours(vertex)):
            color = state.get(edge.destination, None)
            if color == grey:
                raise ValueError("The graph is not a DAG - found a cycle.")
            if color == black:
                continue
            dfs(edge.destination)
        ret.insert(0, vertex)
        state[vertex] = black

    for v in sort(graph.iter_vertices()):
        dfs(v)

    return ret


def test_hamburger():
    peel_onions = 'peel onions'
    chop_onions = 'chop onions'
    fry_onions = 'fry onions'
    grill_patty = 'grill patty'
    put_patty_on_bun = 'put patty on bun'
    put_onion_on_patty = 'put onion on patty'
    put_top_on_bun = 'put_top_on_bun'
    serve = 'serve'

    gr = g.Graph(is_directed=True)
    gr.add_edge(put_top_on_bun, serve)
    gr.add_edge(put_onion_on_patty, put_top_on_bun)
    gr.add_edge(put_patty_on_bun, put_onion_on_patty)
    gr.add_edge(grill_patty, put_patty_on_bun)
    gr.add_edge(fry_onions, put_onion_on_patty)
    gr.add_edge(chop_onions, fry_onions)
    gr.add_edge(peel_onions, chop_onions)

    assert topological_sort(gr, sorted) == [
        'peel onions',
        'grill patty',
        'put patty on bun',
        'chop onions',
        'fry onions',
        'put onion on patty',
        'put_top_on_bun',
        'serve'
    ]


def test_cycle():
    gr = g.Graph(is_directed=True)
    gr.add_edge('a', 'b')
    gr.add_edge('b', 'c')
    gr.add_edge('c', 'a')
    try:
        topological_sort(gr)
    except ValueError:
        pass
    else:
        assert False, 'expected to raise on a cyclic graph'


if __name__ == '__main__':
    test_hamburger()
    test_cycle()
    print('ok')
