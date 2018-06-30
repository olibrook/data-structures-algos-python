import pyalgos.data_structures.trie as t


def test():
    trie = t.Trie()
    trie.set('cat', 'miaow')
    trie.set('dog', 'woof')

    assert trie.get('cat') == 'miaow'
    assert trie.get('dog') == 'woof'

    trie.set('caterpillar', 'rustle')
    assert trie.get('caterpillar') == 'rustle'

    assert sorted(trie.prefix_matches('cat')) == [
        ('cat', 'miaow'),
        ('caterpillar', 'rustle'),
    ]
