import pytest

import pyalgos.puzzles.water_in_a_bar_chart as wbc


cases = (
    ([], 0),
    ([0, 0], 0),
    ([1], 0),
    ([1, 1, 1, 1], 0),
    ([1, 0, 1], 1),
    ([10, 0, 9], 9),
    ([10, 0, 0, 9], 18),
    ([1, 0, 1, 0, 1, 0, 1], 3),
    ([1, 0, 20], 1),
    ([1, 0, 0, 2], 2),
    ([5, 1, 3, 4], 4),
)


@pytest.mark.parametrize('data,expected', cases)
def test(data, expected):
    assert wbc.calculate(data) == expected


