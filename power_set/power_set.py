# O(n*2^n) time | O(n*2^n) space

a = [1, 2, 3, 4,8]


result_lst = [[]]
for i in a:
    lst_len = len(result_lst)
    for idx in range(lst_len):
        idx_ele = result_lst[idx].copy()
        idx_ele.append(i)
        result_lst.append(idx_ele)

print(f"********************* result_lst : {result_lst}")
