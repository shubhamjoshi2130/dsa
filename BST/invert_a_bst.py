import bst


def invert_bst_helper(root):
    if root.left:
        if (root.left.left != None) or (root.left.right != None):
            invert_bst_helper(root.left)

    if root.right:
        if (root.right.left != None) or (root.right.right != None):
            invert_bst_helper(root.right)    
    
    root.left, root.right = root.right, root.left

if __name__ == "__main__":
    print(f"************** Start")
    root = bst.build_tree([2, 1, 3, 5, 4, 8, 90, 6, 70])

    print(f"Before : {root.in_order_traversal()}")
    invert_bst_helper(root)
    print(f"After : {root.in_order_traversal()}")
