import pyalgos.data_structures.hash_table as ht


def test():
    h = ht.HashTable()

    pairs = list(
        ht.Pair(str(i), '{}-{}'.format(i, i))
        for i in range(1000))

    for k, v in pairs:
        h.insert(k, v)

    for k, v in pairs:
        assert h.get(k) == v

    found_pairs = list(h)
    assert len(found_pairs)

    for k, v in pairs:
        h.delete(k)
        assert h.get(k) is None

    assert list(h) == []
