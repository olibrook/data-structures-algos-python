

def fib_gen():
    yield 1
    pp, p = 0, 1
    while True:
        cur = pp + p
        yield cur
        pp, p = p, cur


def fib(n):
    f = fib_gen()
    v = 0
    for i in range(n):
        v = next(f)
    return v


