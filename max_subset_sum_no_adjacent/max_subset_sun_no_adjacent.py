# For given array of +ve integers we need to find out greatest
# sum of 2 numbers without adding adjacent elements


a = [7, 10, 12, 7, 9, 14]


def get_max_sum(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]


def get_max_sum_rec(array):
    return get_max_sum_rec_helpers(array, len(array) - 1)


def get_max_sum_rec_helpers(array, n):
    if n in [0, 1]:
        return array[n]
    else:
        return max(
            get_max_sum_rec_helpers(array, n - 1),
            get_max_sum_rec_helpers(array, n - 2) + array[n],
        )


if __name__ == "__main__":
    print(f"get_max_sum : {get_max_sum(a)}")
    print(f"get_max_sum_rec : {get_max_sum_rec(a)}")
