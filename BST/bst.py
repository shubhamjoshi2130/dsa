import numpy as np

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_branch_sum(self, branch_lst):
        # Not implemented
        if self.data.right:
            branch_sum_right = self.data + self.data.right.find_branch_sum(branch_lst)
        else:
            return self.data
        branch_lst.append(branch_sum_right)

        if self.data.left:
            branch_sum_left = self.data + self.data.left.find_branch_sum(branch_lst)
        else:
            return self.data

        branch_lst.append(branch_sum_left)

    def depth_first_search(self):
        print(self.data)
        if self.left:
            self.left.depth_first_search()

        if self.right:
            self.right.depth_first_search()

    def find_closest(self, data):
        print(f"********************************data: {data}")
        print(f"********************************self.data: {self.data}")
        min_diff = np.abs(self.data - data)
        if not self.right and not self.left:
            return self.data
        min_diff_right = np.abs(self.right.data - data) if self.right else np.inf
        max_diff_left = np.abs(self.left.data - data) if self.left else np.inf

        if (min_diff_right < min_diff) or (max_diff_left < min_diff):
            if min_diff_right < max_diff_left:
                if self.right:
                    return self.right.find_closest(data)
                else:
                    return self.data
            else:
                if self.left:
                    return self.left.find_closest(data)
                else:
                    return self.data
        else:
            return self.data

    def delete(self, data):
        "This retruns what needs to be replaced"
        if self.data > data:
            if self.left:
                self.left.delete(data)
        elif self.data < data:
            if self.right:
                self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

        min_val = self.right.find_min()
        self.data = min_val
        self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
