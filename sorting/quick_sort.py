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


if __name__ == "__main__":
    a = [3, 2, 4, 5, 6, 1, 2, 3]
    quick_sort(a)
    print(f"*************** rotate : {a}")
