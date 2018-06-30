import pyalgos.data_structures.stack as s


def test():
    stack = s.Stack()
    assert stack.is_empty()
    assert stack.peek() is None
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert not stack.is_empty()
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()
