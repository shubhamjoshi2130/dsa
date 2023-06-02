str1 = "abc "
str2 = "yabdac"


def find_levenshtein_distance(str1, str2):
    arr = [[0 for y in range(len(str1) + 1)] for x in range(len(str2) + 1)]

    for i in range(0, len(str1) + 1):
        arr[0][i] = i

    for i in range(1, len(str2) + 1):
        arr[i][0] = i
    # print(f"Length str: {len(arr)}")
    # print(f"Length str[0]: {len(arr[0])}")
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1
    return arr[-1][-1]


if __name__ == "__main__":
    print(
        f"find_levenshtein_distance({str1},{str2}) : {find_levenshtein_distance(str1,str2)}"
    )
