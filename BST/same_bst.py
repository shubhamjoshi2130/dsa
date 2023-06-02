# Check if BST constructed using 2 arrays are same
# without constructing a tree

array1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]


def get_left_and_right(array1, array2):
    array1_left = []
    array1_right = []
    array2_left = []
    array2_right = []

    for i in range(1, len(array1)):
        if array1[i] <= array1[0]:
            array1_left.append(array1[i])
        else:
            array1_right.append(array1[i])

        if array2[i] <= array2[0]:
            array2_left.append(array2[i])
        else:
            array2_right.append(array2[i])
    return array1_left, array1_right, array2_left, array2_right


def check_same_bst_helper(array1, array2):

    # print(f"*** len(array1) : {len(array1)}")
    # print(f"*** len(array2) : {len(array2)}")
    # print(f"*** array1[0] : {array1[0]}")
    # print(f"*** array2[0] : {array2[0]}")

    if len(array1) == 0:
        print(f"************ Inside")
        return True

    if (array1[0] != array2[0]) or (len(array1) != len(array2)):
        return False

    if len(array1) == 1:
        print(f"************ Inside")
        return True

    array1_left, array1_right, array2_left, array2_right = get_left_and_right(
        array1, array2
    )
    return check_same_bst_helper(array1_left, array2_left) and check_same_bst_helper(
        array1_right, array2_right
    )


if __name__ == "__main__":
    print(f"******** : {check_same_bst_helper(array1,array2)}")
