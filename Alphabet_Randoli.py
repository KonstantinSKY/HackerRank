"""https://www.hackerrank.com/challenges/alphabet-rangoli/problem"""

import string


def print_rangoli(size):
    # your code goes here
    letters = string.ascii_lowercase
    pre_list = []
    for i in range(size):
        str_ = letters[i:size]
        pre_list.append("-".join(str_[::-1]+str_[1:]).center(4*size-3, "-"))
    res_list = list(reversed(pre_list))
    res_list.extend(pre_list[1:])
    print("\n".join(res_list))


if __name__ == '__main__':
    print_rangoli(int(input()))




















































