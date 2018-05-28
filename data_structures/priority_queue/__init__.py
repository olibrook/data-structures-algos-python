import data_structures.heap as heap


class _Deleted:
    pass


class PriorityQueue:
    """A PriorityQueue implemented using a heap.

    Uses tombstones to allow removal of tasks and an internal
    counter as a tie-break for two tasks with the same priority.

    """
    def __init__(self):
        self.count = 0
        self.heap = heap.MinHeap()
        self.entries = {}

    def __len__(self):
        return len(self.entries)

    def add(self, task, priority=0):
        entry = [priority, self.count, task]
        self.entries[task] = entry
        self.heap.add(entry)
        self.count += 1

    def remove(self, task):
        entry = self.entries.pop(task)
        entry[-1] = _Deleted

    def pop(self):
        while True:
            priority, count, task = self.heap.pop()
            if task is not _Deleted:
                del self.entries[task]
                return task


if __name__ == '__main__':
    pq = PriorityQueue()

    try:
        pq.pop()
    except:
        pass
    else:
        assert False

    pq.add('t1')
    assert len(pq) == 1
    assert pq.pop() == 't1'

    pq.add('t2', priority=10)
    pq.add('t3', priority=0)
    assert len(pq) == 2
    assert pq.pop() == 't3'
    assert pq.pop() == 't2'
    assert len(pq) == 0

    pq.add('t4', priority=10)
    pq.add('t5', priority=0)
    pq.remove('t5')
    assert len(pq) == 1
    assert pq.pop() == 't4'
    assert len(pq) == 0

    print('Okay')
