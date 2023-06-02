import bst


def max_path_sum(root):
    max_sum = float("-inf")
    _, max_sum = max_path_sum_helper(root, max_sum)
    return max_sum


def max_path_sum_helper(root, max_sum):
    left_sum = 0
    right_sum = 0
    
    
    if root.left:
        left_sum, max_sum = max_path_sum_helper(root.left, max_sum)
        print(f" root.left.data : {root.left.data}")
        
    if root.right:
        right_sum, max_sum = max_path_sum_helper(root.right, max_sum)
        print(f" root.right.data : {root.right.data}")
    
    
    print(f" root.data : {root.data}")
    print(f" left_sum : {left_sum}")
    print(f" right_sum : {right_sum}")
    
    left_sum_root = left_sum + root.data
    right_sum_root = right_sum + root.data

    
    print(f" left_sum_root : {left_sum_root}")
    print(f" right_sum_root : {right_sum_root}")
    print(f" max_sum : {max_sum}")

    max_sum = max(
        left_sum_root, right_sum_root, right_sum + left_sum + root.data, max_sum
    )
    print(f" max_sum after: {max_sum}")

    return max(left_sum_root, right_sum_root), max_sum


if __name__ == "__main__":
    tree = bst.build_tree([2, 1, 7, 6, 5, 4, 3])
    print(f"********** max_path_sum : {max_path_sum(tree)}")
    print(tree.in_order_traversal())
