
class MinHeap:

    def __init__(self):
        self.l = []

    def get_left_child_idx(self, parent_idx):
        return (2 * parent_idx) + 1

    def get_right_child_idx(self, parent_idx):
        return (2 * parent_idx) + 2

    def get_parent_idx(self, child_idx):
        return int((child_idx - 1) / 2)

    def has_parent(self, child_idx):
        return self.get_parent_idx(child_idx) >= 0

    def has_left_child(self, parent_idx):
        return self.get_left_child_idx(parent_idx) < len(self.l)

    def has_right_child(self, parent_idx):
        return self.get_right_child_idx(parent_idx) < len(self.l)

    def left_child(self, parent_idx):
        return self.l[self.get_left_child_idx(parent_idx)]

    def right_child(self, parent_idx):
        return self.l[self.get_right_child_idx(parent_idx)]

    def parent(self, child_idx):
        return self.l[self.get_parent_idx(child_idx)]

    def swap(self, i1, i2):
        tmp = self.l[i1]
        self.l[i1] = self.l[i2]
        self.l[i2] = tmp

    def peek(self):
        # Find-min
        return self.l[0] if len(self.l) else None

    def insert(self):
        pass

    def pop(self):
        pass
