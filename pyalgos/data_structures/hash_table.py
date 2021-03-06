import pyalgos.data_structures.linked_list as ll

import collections

Pair = collections.namedtuple('Pair', ['k', 'v'])


class HashTable:

    def __init__(self):
        num_buckets = 64
        self.buckets = [ll.DoublyLinkedList() for _ in range(num_buckets)]

    def __iter__(self):
        for bucket in self.buckets:
            for ln in bucket:
                yield ln.value

    @staticmethod
    def _key_match(k):
        return lambda pair: pair.k == k

    def hash(self, k):
        return hash(k) % len(self.buckets)

    def insert(self, key, value):
        bucket = self.buckets[self.hash(key)]
        ln = bucket.find(self._key_match(key))
        p = Pair(k=key, v=value)
        if ln:
            ln.value = p
        else:
            bucket.append(p)

    def delete(self, key):
        bucket = self.buckets[self.hash(key)]
        return bucket.splice(bucket.find(self._key_match(key)))

    def get(self, key):
        bucket = self.buckets[self.hash(key)]
        ln = bucket.find(self._key_match(key))
        return ln and ln.value.v
