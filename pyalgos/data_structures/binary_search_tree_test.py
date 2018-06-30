import string
import random

import pyalgos.data_structures.binary_search_tree as _bst


def test():
    bst = _bst.BinarySearchTree()
    items = list(enumerate(string.ascii_letters))
    random.shuffle(items)
    for k, v in items:
        bst.set(k, v)
        assert bst.get(k) == v

    bst = _bst.BinarySearchTree()
    items = list(range(100))
    randomized = items[:]
    random.shuffle(randomized)
    for i in randomized:
        bst.set(i, 'v')
    assert list(bst) == list((i, 'v') for i in items)

    bst = _bst.BinarySearchTree()
    r = list(range(50000))
    random.shuffle(r)
    for i in r:
        bst.set(i, 'v')
    for i in r:
        bst.delete(i)
    assert list(bst) == []
