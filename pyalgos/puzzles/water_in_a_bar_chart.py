"""Calculate the water that would be contained between the towers
in a bar chart, if poured from the top.

This implementation adds each tower to a stack and backtracks
each time a tower is higher than the previous one. By
backtracking to the previous highest tower we can calculate
the volume of water contained up to this new high water mark.

After backtracking, it is possible to compress the data on
the stack as follows:

    volume = 0
    [1, 0, 0, 0, 0, 1]

Can reduce to

    volume = 0
    [1x1, 4x0, 1x1]

After calculating the volume between the 1x1 towers reduce to:

    volume = 4
    [6x1]

Note that water volume is calculated in horizontal, not vertical, slices.

"""
import collections


Line = collections.namedtuple('Line', ['x1', 'x2', 'y'])


def run(data):
    stack = []
    queue = []
    volume = 0
    for x, y in enumerate(data):
        current = Line(x, x + 1, y)
        while stack and stack[-1].y <= current.y:
            queue.insert(0, stack.pop())
        if queue:
            first = queue[0]
            prev = stack[-1] if stack else None
            water_level = current.y if prev and prev.y > first.y else first.y
            while queue:
                popped = queue.pop(0)
                volume += (popped.x2 - popped.x1) * (water_level - popped.y)
            stack.append(Line(first.x1, current.x1, water_level))
        stack.append(current)
    return volume

