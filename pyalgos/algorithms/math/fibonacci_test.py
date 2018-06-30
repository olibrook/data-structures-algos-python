import pyalgos.algorithms.math.fibonacci as f


def test_fib():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    for i, x in enumerate(expected):
        assert f.fib(i) == x
