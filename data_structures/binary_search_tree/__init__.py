
class BST:

    class Node:
        __slots__ = ['left', 'right', 'key', 'value']

        def __init__(self, left=None, right=None, key=None, value=None):
            self.left = left
            self.right = right
            self.key = key
            self.value = value

    def __init__(self):
        self.root = None

    def __iter__(self):
        return self.inorder()

    def inorder(self):
        current = self.root
        stack = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                    yield current.key, current.value
                    current = current.right
                else:
                    break

    def get(self, key):
        curr = self.root
        while curr:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.left if key < curr.key else curr.right
        return None

    def set(self, key, value):
        prev = None
        curr = self.root
        while curr:
            if curr.key == key:
                return curr.value
            else:
                prev = curr
                curr = curr.left if key < curr.key else curr.right

        node = BST.Node(key=key, value=value)
        if not prev:
            self.root = node
        else:
            if key < prev.key:
                prev.left = node
            elif key > prev.key:
                prev.right = node
            else:
                prev.value = value  # Update

    def delete(self):
        pass


if __name__ == "__main__":
    import string
    import random

    bst = BST()
    items = list(enumerate(string.letters))
    random.shuffle(items)
    for k, v in items:
        bst.set(k, v)
        assert bst.get(k) == v

    bst = BST()
    items = list(range(100))
    randomized = items[:]
    random.shuffle(randomized)
    for i in randomized:
        bst.set(i, 'v')
    assert list(bst) == list((i, 'v') for i in items)

    print('Okay')
