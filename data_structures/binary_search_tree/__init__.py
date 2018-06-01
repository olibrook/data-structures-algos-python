

class BinarySearchTree:

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
        raise KeyError(key)

    def set(self, key, value):
        prev = None
        curr = self.root
        while curr:
            if curr.key == key:
                return curr.value
            else:
                prev = curr
                curr = curr.left if key < curr.key else curr.right

        node = BinarySearchTree.Node(key=key, value=value)
        if not prev:
            self.root = node
        else:
            if key < prev.key:
                prev.left = node
            elif key > prev.key:
                prev.right = node
            else:
                prev.value = value  # Update

    def delete(self, key):
        def _delete(k, node):
            if node is None:
                return None
            if k < node.key:
                node.left = _delete(k, node.left)
            elif k > node.key:
                node.right = _delete(k, node.right)
            else:
                if not node.left and not node.right:
                    return None
                elif node.left and not node.right:
                    return node.right
                elif not node.left and node.right:
                    return node.left
                else:
                    # Trickiest case, with both children -
                    # replace this node by copying and then deleting
                    # the successor in its place.
                    successor = self.find_min(node.right)
                    node.key = successor.key
                    node.value = successor.value
                    node.right = _delete(successor.key, node.right)
                    return node

        self.root = _delete(key, self.root)

    @staticmethod
    def find_min(node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr


if __name__ == "__main__":
    def test():
        import string
        import random

        bst = BinarySearchTree()
        items = list(enumerate(string.letters))
        random.shuffle(items)
        for k, v in items:
            bst.set(k, v)
            assert bst.get(k) == v

        bst = BinarySearchTree()
        items = list(range(100))
        randomized = items[:]
        random.shuffle(randomized)
        for i in randomized:
            bst.set(i, 'v')
        assert list(bst) == list((i, 'v') for i in items)

        bst = BinarySearchTree()
        r = list(range(50000))
        random.shuffle(r)
        for i in r:
            bst.set(i, 'v')
        for i in r:
            bst.delete(i)
        assert list(bst) == []

        print('Okay')

    test()
