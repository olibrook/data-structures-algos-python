import pytest

import pyalgos.data_structures.priority_queue as prq


def test():
    queue = prq.PriorityQueue()

    with pytest.raises(Exception):
        queue.pop()

    queue.add('t1')
    assert len(queue) == 1
    assert queue.pop() == 't1'

    queue.add('t2', priority=10)
    queue.add('t3', priority=0)
    assert len(queue) == 2
    assert queue.pop() == 't3'
    assert queue.pop() == 't2'
    assert len(queue) == 0

    queue.add('t4', priority=10)
    queue.add('t5', priority=0)
    queue.remove('t5')
    assert len(queue) == 1
    assert queue.pop() == 't4'
    assert len(queue) == 0
