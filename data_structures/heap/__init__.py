import collections


Pair = collections.namedtuple('Pair', ['idx', 'v'])


class MinHeap:

    def __init__(self):
        self.l = []

    def left_child(self, idx):
        c_idx = (2 * idx) + 1
        return Pair(c_idx, self.l[c_idx]) if c_idx < len(self.l) else None

    def right_child(self, idx):
        c_idx = (2 * idx) + 2
        return Pair(c_idx, self.l[c_idx]) if c_idx < len(self.l) else None

    def parent(self, idx):
        p_idx = int((idx - 1) / 2)
        return Pair(p_idx, self.l[p_idx]) if p_idx >= 0 else None

    def children(self, idx):
        ret = (self.left_child(idx), self.right_child(idx))
        ret = (x for x in ret if x is not None)
        return list(ret)

    def swap(self, i1, i2):
        tmp = self.l[i1]
        self.l[i1] = self.l[i2]
        self.l[i2] = tmp

    def peek(self):
        return self.l[0] if len(self.l) else None

    def pop(self):
        item = self.l.pop(0) if len(self.l) else None
        if len(self.l):
            self.l.insert(0, self.l.pop())
            self.heapify_down()
        return item

    def add(self, v):
        self.l.append(v)
        self.heapify_up()

    def heapify_up(self):
        # Take the last element of the heap and lift it up until we reach a
        # parent with a value less then the current one.
        if len(self.l):
            current_idx = len(self.l) - 1
            while True:
                parent = self.parent(current_idx)
                if parent is None or self.l[current_idx] >= parent.v:
                    break
                else:
                    self.swap(current_idx, parent.idx)
                    current_idx = parent.idx

    def heapify_down(self):
        # Compare the root element to its children and swap root with the smallest
        # of children. Do the same for next children after swap.
        if len(self.l):
            current_idx = 0
            while True:
                children = self.children(current_idx)
                smallest = (
                    min(children, key=lambda pair: pair.v) if children
                    else None)
                if smallest is None or self.l[current_idx] < smallest.v:
                    break
                self.swap(current_idx, smallest.idx)
                current_idx = smallest.idx


if __name__ == '__main__':
    h = MinHeap()
    h.add(1)
    assert h.pop() == 1
    h.add(3)
    h.add(1)
    h.add(1)
    h.add(1)
    h.add(1)
    h.add(2)
    assert h.pop() == 1
    assert h.pop() == 1
    assert h.pop() == 1
    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 3
    assert h.pop() is None

    print('Okay')
