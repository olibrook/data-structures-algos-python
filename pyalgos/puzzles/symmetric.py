#!/usr/bin/env python3

import itertools


class TreeNode:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []


def level_order(node, left_to_right=True):
    """Level-order tree-traversal, supporting level-traversal from left or right"""
    items = iter([node])
    fn = iter if left_to_right else reversed

    while True:
        current = next(items)  # Breaks the loop on StopIteration
        yield current
        items = itertools.chain(items, fn(current.children))


class Empty:
    pass


def equal(it1, it2):
    """Return true if two iterators are equal"""
    return all(x == y for x, y in itertools.zip_longest(it1, it2, fillvalue=Empty))


def run(node):
    """Return True if the tree rooted at `node` is symmetric.

    Method:

    Compare the outermost left and right children of `node` in turn,
    working inwards. Compare subtrees by a level-order tree traversal taken
    left-to-r for nodes on the left and right-to-left nodes on the right.

    If `node` has an odd number of children, the child at the center must
    itself be a symmetric tree for `node` to be considered symmetric. This
    handles both the odd-number of children and single-child edge-cases.

    """
    i = 0
    _max = int((len(node.children) + 1) / 2)
    symmetric = True
    while symmetric and i < _max:
        l_node = node.children[i]
        r_node = node.children[-1 - i]
        l_items = (x.value for x in level_order(node, left_to_right=True))
        r_items = (x.value for x in level_order(node, left_to_right=False))
        symmetric = (
            l_node is r_node and (run(l_node)) or equal(l_items, r_items)
        )
        i += 1
    return symmetric
