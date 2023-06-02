# Travers a given array in zigzag travers

arr = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]


def zig_zag_travers(arr):
    i = 0
    j = 0
    total_elements = len(arr) * len(arr[0])
    k = 0
    up = False
    max_row_idx = len(arr) - 1
    max_col_index = len(arr[0]) - 1
    while k < (total_elements):
        # print(f"arr[{i}][{j}] : ")
        print(f"arr[{i}][{j}] : {arr[i][j]}")

        if (j == 0) and (i % 2 == 0) and (i != max_row_idx):
            i += 1
            up = True
        elif ((i == 0) and (j % 2 != 0)) and (j != max_col_index):
            j += 1
            up = False
        elif (j == max_col_index) and (i % 2 == 0):
            i += 1
            up = False
        elif (i == max_row_idx) and (j % 2 != 0):
            j += 1
            up = True
        elif up:
            i -= 1
            j += 1
        else:
            j -= 1
            i += 1
        k += 1


if __name__ == "__main__":
    print(f"***************** :{zig_zag_travers(arr)} ")
