import data_structures.linked_list as ll

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


if __name__ == '__main__':
    lru = LRUCache(size=2)
    lru.set('foo', 'bar')
    assert lru.get('foo') == 'bar'
    assert sorted(lru.cache.keys()) == ['foo']
    assert [x.value for x in lru.list.items()] == [('foo', 'bar')]

    lru.set('biz', 'baz')
    assert lru.get('biz') == 'baz'
    assert sorted(lru.cache.keys()) == ['biz', 'foo']
    assert [x.value for x in lru.list.items()] == [('biz', 'baz'), ('foo', 'bar')]

    assert lru.get('foo') == 'bar'  # Expect "biz" to now be least recently used
    assert sorted(lru.cache.keys()) == ['biz', 'foo']
    assert [x.value for x in lru.list.items()] == [('foo', 'bar'), ('biz', 'baz')]

    lru.set('wiz', 'waz')
    assert lru.get('wiz') == 'waz'
    # Expect biz to be evicted and len() of cache and linked-list to be 2
    assert sorted(lru.cache.keys()) == ['foo', 'wiz']
    assert [x.value for x in lru.list.items()] == [('wiz', 'waz'), ('foo', 'bar')]

    print(lru.cache)
    print(lru.list)
    print('Okay')
