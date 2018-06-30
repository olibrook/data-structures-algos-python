
class Trie:

    class Node:
        def __init__(self):
            self.children = {}
            self.value = None
            self.terminal = False

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
            if char not in node.children:
                node.children[char] = Trie.Node()
            node = node.children[char]
        node.value = value  # Store value at leaf
        node.terminal = True

    def prefix_matches(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        ret = []
        stack = [(prefix, node)]
        while stack:
            prefix, node = stack.pop()
            for char, child_node in node.children.items():
                stack.append((prefix + char, child_node))
            if node.terminal:  # Current prefix is a complete key
                ret.append((prefix, node.value))
        return ret
