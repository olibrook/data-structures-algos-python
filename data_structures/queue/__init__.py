import data_structures.linked_list as linked_list


class Queue:

    def __init__(self):
        self.ll = linked_list.DoublyLinkedList()

    def __unicode__(self):
        return '<{} {}>'.format(
            self.__class__.__name__, list(self.ll))

    def is_empty(self):
        return self.ll.head is None

    def peek(self):
        return self.ll.head and self.ll.head.value

    def enqueue(self, value):
        return self.ll.append(value)

    def dequeue(self):
        return self.ll.delete_head()


if __name__ == '__main__':
    q = Queue()
    assert q.is_empty()
    assert q.peek() is None
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert not q.is_empty()
    assert q.peek() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()

    print('OK')
