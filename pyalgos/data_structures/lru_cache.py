import pyalgos.data_structures.linked_list as ll

import collections

Pair = collections.namedtuple('Pair', ['k', 'v'])


class LRUCache:
    """An LRU Cache with a default size of 10 and constant-time get/set ops"""
    def __init__(self, size=10):
        self.size = size
        self.cache = {}
        self.list = ll.DoublyLinkedList()

    def set(self, k, v):
        if len(self.cache) >= self.size:
            del self.cache[self.list.delete_tail().k]
        ln = ll.Node(value=Pair(k, v))
        self.list.prepend_node(ln)
        self.cache[k] = ln

    def get(self, k):
        ln = self.cache.get(k)
        if ln:
            self.list.splice(ln)
            self.list.prepend_node(ln)
            return ln.value.v
        else:
            return None
