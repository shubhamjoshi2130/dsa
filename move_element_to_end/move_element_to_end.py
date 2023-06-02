# given array of elements and an element ,
# find all instances of the number in the and move it to end
# this need to be done in inplace, no new array should be created


def move_to_end_rotation(arr_in, ele):
    """
    Using nested loop O(n^2)
    """
    arr_len = len(arr_in)
    idx = 0
    while idx < arr_len:
        print(f"***** before: {arr_in[idx]}")
        if arr_in[idx] == ele:
            print(f"################ Chokri")
            temp = arr_in[idx]
            print(f" after array : {arr_in}")
            for i in range(idx, arr_len - 1):
                print(f"################ i : {i}")
                arr_in[i] = arr_in[i + 1]
            print(f" after array : {arr_in}")
            arr_in[arr_len - 1] = temp
            arr_len = arr_len - 1
        print(f"############### idx : {idx} , arr_in[idx] : {arr_in[idx]}, ele : {ele}")
        if arr_in[idx] != ele:
            print(f"***** after: {arr_in[idx]}")
            idx += 1


def move_to_end_pointer(arr_in, ele):
    """
    Using pointers O(n)
    """
    arr_len = len(arr_in)
    right_idx = arr_len - 1
    left_idx = 0

    while arr_in[right_idx] == ele:
        right_idx -= 1

    while left_idx < right_idx:
        if arr_in[left_idx] == ele:
            arr_in[left_idx], arr_in[right_idx] = arr_in[right_idx], arr_in[left_idx]
            right_idx -= 1

        if arr_in[left_idx] != ele:
            left_idx += 1


if __name__ == "__main__":
    a = [2, 1, 2, 2, 2, 3, 4, 2]
    ele = 2
    move_to_end_pointer(a, ele)
    print(a)
