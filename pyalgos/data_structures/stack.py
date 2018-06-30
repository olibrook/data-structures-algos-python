import pyalgos.data_structures.linked_list as linked_list


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
