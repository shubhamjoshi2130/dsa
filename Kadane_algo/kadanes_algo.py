# Find max sum of sub array

arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]


def get_max_sum(array):
    return get_max_sum_helper(array, len(array) - 1, array[0])[1]


def get_max_sum_helper(array, n, max_so_far):
    if n == 0:
        return array[0], array[0]
    else:
        max_nm1, max_so_far = get_max_sum_helper(array, n - 1, max_so_far)
        max_n = max(max_nm1 + array[n], array[n])
        max_so_far = max(max_n, max_so_far)
        return max_n, max_so_far


def kadanesAlgo(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar


if __name__ == "__main__":
    print(f"get_max_sum({arr}) : {get_max_sum(arr)}")
    print(f"kadanesAlgo({arr}) : {kadanesAlgo(arr)}")
