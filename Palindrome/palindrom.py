str = "110011"


def palindrome(str):
    for i in range(int(len(str) / 2)):
        print(i)
        print(f"********** str[{i}] : {str[i]}")
        print(f"********** str[{-(i+1)}] : {str[-(i+1)]}")

        if str[i] != str[-(i + 1)]:
            return False
    return True


def palindrome_rec_fun(str_in):
    return palindrome_rec(str_in, 0, len(str_in) - 1)


def palindrome_rec(str_in, left_idx, right_idx):
    if str_in[left_idx] != str_in[right_idx]:
        return False
    else:
        return palindrome_rec(str_in, left_idx + 1, right_idx - 1)


if __name__ == "__main__":
    print(f"*************** palindrome : {palindrome(str)}")
    print(f"*************** palindrome : {palindrome_rec_fun(str)}")
