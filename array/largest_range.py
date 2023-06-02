# Given an array we need to find the largest range

arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# Answer should be [0,7], viz max sequence of cntinueous numbers


def get_max_range(arr):
    max_num = float("inf")
    min_num = float("-inf")

    for i in range(len(arr)):
        if max_num >= arr[i]:
            max_num = arr[i]

        if min_num <= arr[i]:
            min_num = arr[i]
    return max_num, min_num


def get_max_range_continueous(arr):
    num_dict = {}
    for i in range(len(arr)):
        num_dict[arr[i]] = True

    final_left = float("inf")
    final_right = float("-inf")
    print(f"*** final diff : {final_right - final_left}")
    for i in range(0, len(arr)):

        left = arr[i]
        right = arr[i]

        check_left_num = arr[i] - 1

        while num_dict.get(check_left_num, False) and (check_left_num >= final_right):
            if check_left_num == final_right:
                left = final_left
                break
            left = check_left_num
            check_left_num -= 1

        check_right_num = arr[i] + 1

        while num_dict.get(check_right_num, False) and (check_right_num <= final_left):
            if check_right_num == final_left:
                right = final_right
                break
            right = check_right_num
            check_right_num += 1

        if (final_right - final_left) < (right - left):
            final_right = check_right_num - 1
            final_left = check_left_num + 1
    return final_left, final_right


if __name__ == "__main__":
    print(f"**************** : {get_max_range_continueous(arr)}")
