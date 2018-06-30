import pytest

import pyalgos.data_structures.heap as h


def test():
    heap = h.MinHeap()
    heap.add(1)
    assert heap.peek() == 1
    assert heap.pop() == 1
    heap.add(3)
    heap.add(1)
    heap.add(1)
    heap.add(1)
    heap.add(1)
    heap.add(2)
    assert heap.pop() == 1
    assert heap.pop() == 1
    assert heap.pop() == 1
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3

    with pytest.raises(Exception):
        heap.peek()

    with pytest.raises(Exception):
        heap.pop()
