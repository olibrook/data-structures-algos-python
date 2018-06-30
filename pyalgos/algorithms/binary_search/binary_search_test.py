import pyalgos.algorithms.binary_search.binary_search as bs

def test():
    assert bs.binary_search([], 'a') == -1
    assert bs.binary_search(['a'], 'a') == 0
    assert bs.binary_search(['a', 'b'], 'b') == 1
    assert bs.binary_search(['a'] * 50, 'a') == 0
