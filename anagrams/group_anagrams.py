# group anagrams in a list

ang = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]


def group_anagrams(ana):
    result_dict = dict()
    ana_sorted = ["".join(sorted(x)) for x in ana]
    print(f"********** {ana_sorted}")
    for k, agram in enumerate(ana):
        print(f"************* agram: {agram}")
        agram_lst = result_dict.get(ana_sorted[k], None)
        if agram_lst != None:
            agram_lst.append(agram)
        else:
            result_dict[ana_sorted[k]] = [agram]
    print(f" **** dict: {result_dict}")
    return result_dict.values()


if __name__ == "__main__":
    print(f"group_anagrams({ang}) : {group_anagrams(ang)}")
