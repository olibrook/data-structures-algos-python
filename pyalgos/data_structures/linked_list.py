class Node:

    __slots__ = 'value', 'prev', 'next'

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __unicode__(self):
        return '<Node {}>'.format(self.value)

    def __repr__(self):
        return self.__unicode__()


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __unicode__(self):
        return '<{} {}>'.format(
            self.__class__.__name__, list(self))

    def __repr__(self):
        return self.__unicode__()

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def items(self):
        return list(self)

    def splice(self, ln):
        if ln:
            if not isinstance(ln, Node):
                raise RuntimeError()
            if ln.prev:
                ln.prev.next = ln.next
            if ln.next:
                ln.next.prev = ln.prev
            if ln is self.head:
                self.head = ln.next
            if ln is self.tail:
                self.tail = ln.prev
            ln.next = None
            ln.prev = None
        return ln

    def prepend(self, value):
        self.prepend_node(Node(value=value))

    def prepend_node(self, ln):
        ln.next = self.head
        ln.prev = None
        self.head = ln
        if self.head.next:
            self.head.next.prev = self.head
        if not self.tail:
            self.tail = self.head

    def append(self, value):
        self.append_node(Node(value=value))

    def append_node(self, ln):
        ln.prev = self.tail
        ln.next = None
        self.tail = ln
        if self.tail.prev:
            self.tail.prev.next = self.tail
        if not self.head:
            self.head = self.tail

    def delete(self, value):
        ln = self.find(value)
        if ln:
            self.splice(ln)
            return ln.value
        return None

    def find(self, value):
        """Return the node matching value, which is a val or predicate"""
        predicate = value if callable(value) else lambda v: v == value
        for x in self:
            if predicate(x.value):
                return x
        return None

    def delete_tail(self):
        ln = self.splice(self.tail)
        return ln.value if ln else None

    def delete_head(self):
        ln = self.splice(self.head)
        return ln.value if ln else None
