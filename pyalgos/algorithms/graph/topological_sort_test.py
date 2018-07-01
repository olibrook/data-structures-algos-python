import pytest

import pyalgos.data_structures.graph as g
import pyalgos.algorithms.graph.topological_sort as t


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

    assert t.topological_sort(gr) == [
        peel_onions,
        chop_onions,
        fry_onions,
        grill_patty,
        put_patty_on_bun,
        put_onion_on_patty,
        put_top_on_bun,
        serve
    ]


def test_cycle():
    gr = g.Graph(is_directed=True)
    gr.add_edge('a', 'b')
    gr.add_edge('b', 'c')
    gr.add_edge('c', 'a')
    with pytest.raises(Exception):
        t.topological_sort(gr)
