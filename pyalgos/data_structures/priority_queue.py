import pyalgos.data_structures.heap as heap


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
