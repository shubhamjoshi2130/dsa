"""Find a number in sorted 2d array
O
"""

a = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]


length = len(a)
width = len(a[0])

row_idx = 0
col_idx = width - 1
ele = 555

while row_idx < length:
    if a[row_idx][col_idx] > ele:
        col_idx -= 1
    elif a[row_idx][col_idx] == ele:
        print("!!! Found !!!")
        break
    else:
        row_idx += 1
