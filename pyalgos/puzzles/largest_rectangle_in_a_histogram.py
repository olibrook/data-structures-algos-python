"""Largest rectangle in a histogram.

Key to this problem is using a stack to keep track of top-left
corners that could be used when shading a rectangle.

Every time we see a > value than the last, it adds a new potential top-left
corner that we need to keep track of. To keep track of them, put values on a stack
maintaining the invariant that higher stack entries have higher values.

Every time the invariant would be violated we can discard stack entries, reducing the
number of areas we need to compute for each subsequent value.

Note that in the following sequence:

  [1, 2, 3, 4, 5, 0]

The presence of the 0 in the last position makes all previous values no longer
candidates for the top-left corner.

"""
import collections


Point = collections.namedtuple('Point', ['x', 'y'])


def find(data):
    largest = 0
    stack = []
    current = None
    for x, y in enumerate(data):
        current = Point(x, y)
        popped = None
        while stack and current.y <= stack[-1].y:
            popped = stack.pop()
            largest = max(largest, popped.y * (current.x - popped.x))

        l = popped.x if popped else current.x
        stack.append(Point(l, current.y))

    while stack and current:
        popped = stack.pop()
        largest = max(largest, popped.y * (current.x+1 - popped.x))

    return largest
