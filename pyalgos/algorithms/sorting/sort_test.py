import pytest

import pyalgos.algorithms.sorting.insertion as insertion
import pyalgos.algorithms.sorting.selection as selection
import pyalgos.algorithms.sorting.bubble as bubble
import pyalgos.algorithms.sorting.heap as heap
import pyalgos.algorithms.sorting.merge as merge
import pyalgos.algorithms.sorting.quick as quick


methods = [
    insertion,
    selection,
    bubble,
    heap,
    merge,
    quick,
]


@pytest.mark.parametrize('method', methods)
def test(method):
    actual = method.sort(list(reversed(range(573))))
    expected = list(range(573))
    assert actual == expected
    assert method.sort([]) == []
