"""Find longest substring palindrome
"""

import palindrom as pal


def find_longest_palindrome_helper(str_in):
    n = len(str_in)
    if n == 1:
        return str_in[0]
    final_right = 0
    final_left = 0
    for i in range(1, n):
        final_right, final_left = check_pal_helper(str_in, i, final_right, final_left)
    return str_in[final_left : final_right + 1]


def check_pal_helper(str_in, i, final_right, final_left):
    # Taking i as center

    str_len = len(str_in) - 1
    odd_left_idx = i - 1
    odd_right_idx = i + 1

    even_left_idx = i - 1
    even_right_idx = i

    break_odd = False
    break_even = False
    while (even_left_idx >= 0) and (even_right_idx <= min(2 * i, str_len)):
        if (
            (odd_right_idx <= min(2 * i - 1, str_len))
            and (odd_left_idx >= 0)
            and (not break_odd)
        ):
            # print(f" str_in[odd_left_idx] : {str_in[odd_left_idx]} ")
            # print(f" str_in[odd_right_idx] : {str_in[odd_right_idx]} ")
            print(f"odd_left_idx : {odd_left_idx} , odd_right_idx : {odd_right_idx}")
            if str_in[odd_left_idx] == str_in[odd_right_idx]:
                odd_left_idx -= 1
                odd_right_idx += 1
                # break_odd = False
            else:
                break_odd = True
            # print(f" break_odd : {break_odd} ")
        else:
            break_odd = True

        print(f" break_odd {i}: {break_odd} ")
        # break
        if not break_even:
            if (str_in[even_left_idx] == str_in[even_right_idx]) and (not break_even):
                even_left_idx -= 1
                even_right_idx += 1
                # break_even = False
            else:
                break_even = True
        print(f" break_even {i} : {break_even} ")
        if break_even and break_odd:
            break

    if (final_right - final_left) < (odd_right_idx - odd_left_idx - 2):
        final_right, final_left = odd_right_idx - 1, odd_left_idx + 1

    if (final_right - final_left) < (even_right_idx - even_left_idx - 2):
        final_right, final_left = even_right_idx - 1, even_left_idx + 1

    return final_right, final_left


if __name__ == "__main__":
    a_str = "abaxyzazyxf"
    print(
        f"find_longest_palindrome_helper({a_str}) : {find_longest_palindrome_helper(a_str)}"
    )
