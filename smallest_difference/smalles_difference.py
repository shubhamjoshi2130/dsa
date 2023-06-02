# Find the 2 closest numbers from 2 arrays

a = [-1, 5, 10, 20, 26, 28, 3, 17]
b = [26, 134, 135, 15, 17]


def quick_sort_loop(array_in, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    pivot = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx
    while left_idx <= right_idx:
        print(f"******************** pivot : {pivot}")
        print(f"******************** left_idx : {left_idx}")
        print(f"******************** right_idx : {right_idx}")

        if (array_in[left_idx] > array_in[pivot]) and (
            array_in[right_idx] < array_in[pivot]
        ):
            array_in[left_idx], array_in[right_idx] = (
                array_in[right_idx],
                array_in[left_idx],
            )

        if array_in[left_idx] <= array_in[pivot]:
            left_idx += 1

        if array_in[right_idx] >= array_in[pivot]:
            right_idx -= 1

    print(f"###******************** pivot : {pivot}")
    print(f"###******************** left_idx : {left_idx}")
    print(f"###******************** right_idx : {right_idx}")
    array_in[right_idx], array_in[pivot] = array_in[pivot], array_in[right_idx]

    if (right_idx - 1 - start_idx) < (end_idx - right_idx + 1):
        quick_sort_loop(array_in, start_idx, right_idx - 1)
        quick_sort_loop(array_in, right_idx + 1, end_idx)
    else:
        quick_sort_loop(array_in, right_idx + 1, end_idx)
        quick_sort_loop(array_in, start_idx, right_idx - 1)


def quick_sort(array_in):
    start_idx = 0
    end_idx = len(array_in) - 1
    return quick_sort_loop(array_in, start_idx, end_idx)


def smallest_diff_helper(a, b):
    a_p = 1
    b_p = 1
    diff = b[0] - a[0]
    final_a = a[0]
    final_b = b[0]

    while a_p < len(a) and b_p < len(b):
        temp_diff = b[b_p] - a[a_p]
        if temp_diff < diff:
            final_a = a[a_p]
            final_b = b[b_p]
            diff = temp_diff

        if a[a_p] < b[b_p]:
            a_p += 1
        else:
            b_p += 1
    return final_a, final_b


def smallest_difference(a, b):
    a = quick_sort(a)
    b = quick_sort(b)
    print(f"****** a: {a}")
    print(f"****** b: {b}")


if __name__ == "__main__":
    a.sort()
    b.sort()
    print(f"*************** smallest_diff_helper : {smallest_diff_helper(a,b)}")
