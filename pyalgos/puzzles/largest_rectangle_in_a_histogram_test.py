import pytest

import pyalgos.puzzles.largest_rectangle_in_a_histogram as largest


cases = (
    ([], 0),
    ([2], 2),
    ([2, 1, 1, 1], 4),
    ([2, 1, 5], 5),
    ([2, 1, 5, 6], 10),
    ([2, 1, 5, 6, 2, 3], 10),
    ([1, 1, 1, 1, 1, 1, 0, 10], 10),
    ([1, 2, 3, 4, 5, 6, 0, 10], 12),
    ([10, 0, 6, 5, 4, 3, 2, 1], 12),
)


@pytest.mark.parametrize('data,expected', cases)
def test(data, expected):
    assert largest.find(data) == expected


