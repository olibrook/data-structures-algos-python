import data_structures.linked_list as linked_list


class Stack:

    def __init__(self):
        self.ll = linked_list.DoublyLinkedList()

    def __unicode__(self):
        return '<{} {}>'.format(
            self.__class__.__name__, list(self.ll))

    def is_empty(self):
        return self.ll.head is None

    def peek(self):
        return self.ll.head and self.ll.head.value

    def push(self, value):
        return self.ll.prepend(value)

    def pop(self):
        return self.ll.delete_head()


if __name__ == '__main__':
    s = Stack()
    assert s.is_empty()
    assert s.peek() is None
    s.push(1)
    s.push(2)
    s.push(3)
    assert not s.is_empty()
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()

    print('OK')
