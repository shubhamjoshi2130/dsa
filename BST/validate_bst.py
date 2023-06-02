# Validate binary searh tree
import sys

sys.path.append("E:\\DSA\\BST")

import bst


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True

    if tree.value < minValue or tree.value >= maxValue:
        return False

    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


if __name__ == "__main__":
    print(f"********************")
    pass
