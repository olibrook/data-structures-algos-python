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


def is_symmetric(node):
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
            l_node is r_node and (is_symmetric(l_node)) or equal(l_items, r_items)
        )
        i += 1
    return symmetric


def main():
    _ = TreeNode

    # Single
    assert is_symmetric(_('a'))

    # Single chain
    assert is_symmetric(
        _('a', [
            _('b', [
                _('c')
            ])
        ])
    )

    assert not is_symmetric(
        _('a', [
            _('b'),
            _('c'),
        ])
    )

    assert is_symmetric(
        _('a', [
            _('b'),
            _('b'),
        ])
    )

    assert is_symmetric(
        _('a', [
            _('b'),
            _('c'),
            _('b'),
        ])
    )

    assert not is_symmetric(
        _('a', [
            _('b'),
            _('c'),
            _('c'),
        ])
    )

    assert is_symmetric(
        _('a', [
            _('b', [
                _('c', [
                    _('d', [
                        _('e')
                    ])
                ])
            ]),
            _('c'),
            _('b', [
                _('c', [
                    _('d', [
                        _('e')
                    ])
                ])
            ]),
        ])
    )

    assert is_symmetric(
        _('a', [
            _('b', [
                _('c', [
                    _('d', [
                        _('e'), _('f')
                    ])
                ])
            ]),
            _('c'),
            _('b', [
                _('c', [
                    _('d', [
                        _('f'), _('e')
                    ])
                ])
            ]),
        ])
    )

    # Check proper handling of center nodes
    assert is_symmetric(
        _('a', [
            _('b'),
            _('c', [
                _('d'),
                _('d'),
            ]),
            _('b'),
        ])
    )

    assert not is_symmetric(
        _('a', [
            _('b'),
            _('c', [
                _('d'),
                _('e'),
            ]),
            _('b'),
        ])
    )
    print('ok')


if __name__ == '__main__':
    main()
