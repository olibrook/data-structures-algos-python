import collections


Pair = collections.namedtuple('Pair', ['idx', 'v'])


class MinHeap:

    def __init__(self):
        self.l = []

    def __len__(self):
        return len(self.l)

    def item_at(self, idx):
        return 0 <= idx < len(self.l) and Pair(idx, self.l[idx]) or None

    def left_child(self, idx):
        return self.item_at((2 * idx) + 1)

    def right_child(self, idx):
        return self.item_at((2 * idx) + 2)

    def parent(self, idx):
        return self.item_at(int((idx - 1) / 2))

    def children(self, idx):
        ret = (self.left_child(idx), self.right_child(idx))
        ret = (x for x in ret if x is not None)
        return list(ret)

    def swap(self, i1, i2):
        tmp = self.l[i1]
        self.l[i1] = self.l[i2]
        self.l[i2] = tmp

    def peek(self):
        return self.l[0]

    def pop(self):
        item = self.l.pop(0)
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
            current = self.item_at(len(self.l) - 1)
            while True:
                parent = self.parent(current.idx)
                if parent is None or current.v >= parent.v:
                    break
                else:
                    self.swap(current.idx, parent.idx)
                    current = parent

    def heapify_down(self):
        # Compare the root element to its children and swap root with the smallest
        # of children. Do the same for next children after swap.
        if len(self.l):
            current = self.item_at(0)
            while True:
                children = self.children(current.idx)
                smallest = (
                    min(children, key=lambda pair: pair.v) if children else None)
                if smallest is None or current.v < smallest.v:
                    break
                self.swap(current.idx, smallest.idx)
                current = smallest


if __name__ == '__main__':
    h = MinHeap()
    h.add(1)
    assert h.peek() == 1
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

    for m in (h.peek, h.pop):
        try:
            m()
        except:
            pass
        else:
            assert False

    print('Okay')
