from io import StringIO


# for i in range(len(mylist)):
#     file_str.write(mylist[i])
# print(file_str.getvalue())

str_in = "xyz"


def rotate(str_in, n):
    range = 122 - 97
    if n > range:
        n = n - range
    file_str = StringIO()
    for i in str_in:
        nLC = ord(i) + n
        if nLC > 122:
            nLC = 96 + nLC % 122
        file_str.write(chr(nLC))

    return file_str.getvalue()


if __name__ == "__main__":
    print(f"*************** rotate : {rotate('xyz',10)}")
