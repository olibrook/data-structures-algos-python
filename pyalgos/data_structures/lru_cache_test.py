import pyalgos.data_structures.lru_cache as l


def test():
    lru = l.LRUCache(size=2)
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
