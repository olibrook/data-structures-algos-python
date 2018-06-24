

def fib_gen():
    """The infinite fibonacci sequence"""
    yield 1
    l = [0, 1]
    while True:
        cur = sum(l)
        yield cur
        l[0] = l[1]
        l[1] = cur


def fib(n):
    """Get the nth fibonacci number"""
    f = fib_gen()
    v = 0
    for i in range(n):
        v = next(f)
    return v


