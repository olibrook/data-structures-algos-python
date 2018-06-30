import pyalgos.data_structures.queue as q


def test():
    queue = q.Queue()
    assert queue.is_empty()
    assert queue.peek() is None
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert not queue.is_empty()
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()
