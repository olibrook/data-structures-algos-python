import collections


Line = collections.namedtuple('Line', ['x1', 'x2', 'y'])


def calculate(data):
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

