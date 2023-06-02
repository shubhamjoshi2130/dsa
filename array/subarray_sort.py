# Given an array with n numbers not sorted. If we sort those
# the whole array gets sorted

arr = [1, 2, 3, 5, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19, 4]


def subArraySort(arr):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    start_index = -1
    end_idx = 0

    if arr[0] > arr[1]:
        start_index = 0
        minOutOfOrder = min(minOutOfOrder, arr[0])
        maxOutOfOrder = max(maxOutOfOrder, arr[0])

    if arr[-1] < arr[-2]:
        end_idx = len(arr) - 1
        minOutOfOrder = min(minOutOfOrder, arr[-1])
        maxOutOfOrder = max(maxOutOfOrder, arr[-1])

    print(f"*************** end_idx: {end_idx}")
    for i in range(1, len(arr) - 2):
        if not arr[i - 1] <= arr[i] <= arr[i + 1]:
            if start_index == -1:
                start_index = i
            minOutOfOrder = min(minOutOfOrder, arr[i])
            maxOutOfOrder = max(maxOutOfOrder, arr[i])
            if end_idx < i:
                end_idx = i
    print(f"*************** end_idx: {end_idx}")
    print(f"*************** start_index: {start_index}")
    print(f"*************** minOutOfOrder: {minOutOfOrder}")
    print(f"*************** maxOutOfOrder: {maxOutOfOrder}")
    final_start = start_index
    for i in range(start_index, -1, -1):
        if arr[i] >= minOutOfOrder:
            final_start = i

    final_end = end_idx
    for i in range(final_end, len(arr)):
        if arr[i] <= maxOutOfOrder:
            final_end = i

    print(f"*************** final_end: {final_end}")
    return arr[final_start : final_end + 1]


if __name__ == "__main__":
    print(f"******************** : {subArraySort(arr)}")
