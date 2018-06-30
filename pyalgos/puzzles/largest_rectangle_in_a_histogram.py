"""Largest rectangle in a histogram.

Key to this problem is using a stack to keep track of the potential top-left
corners that could be used when shading a rectangle.

Every time we see a > value than the last, it adds a new potential top-left
corner that we need to keep track of.

Every time we see a <= value than the last, we can discard candidates on the
stack, reducing the number of areas we need to compute for each subsequent value.

Note that in the following sequence:

  [1, 2, 3, 4, 5, 0]

The presence of the 0 in the last position makes all previous values no longer
candidates for the top-left corner.

"""
import itertools
import collections


Point = collections.namedtuple('Point', ['x', 'y'])


def coroutine():
    """Coroutine implementation allows computation eg. from an iterator of values.

    Call next() and then send() with each new val to get the current max-rect.

    """
    largest = 0
    stack = []
    x = 0
    while True:
        y = yield
        current = Point(x, y)
        popped = None
        while stack and current.y <= stack[-1].y:
            popped = stack.pop()

        if popped:
            stack.append(Point(popped.x, current.y))

        if not stack or stack[-1].y < current.y:
            stack.append(current)

        areas = (
            min(left.y, current.y) * (current.x+1 - left.x)
            for left in stack
        )
        areas = itertools.chain(areas, [largest])
        largest = max(areas)
        yield largest
        x += 1


def find(data):
    """Find-max for a list of values"""
    largest = 0
    coro = coroutine()
    for y in data:
        next(coro)
        largest = coro.send(y)
    return largest
