

class Trie:

    class Node:
        def __init__(self):
            self.children = {}
            self.value = None

    def __init__(self):
        self.root = Trie.Node()

    def get(self, key):
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value

    def set(self, key, value):
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                node = Trie.Node()
                node.children[char] = node
        node.value = value  # Store value at leaf

    def suggestions(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        return self.collect_terminals(node)

    @staticmethod
    def collect_terminals(node):
        ret = []
        stack = [node]
        while stack:
            n = stack.pop()
            stack.extend(n.children)
            if not n.children:  # Terminal
                ret.append(node.value)
        return ret


if __name__ == '__main__':
    t = Trie()
    t.set('cat', 'cat')
