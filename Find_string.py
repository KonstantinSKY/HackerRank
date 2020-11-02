"""https://www.hackerrank.com/challenges/find-a-string/problem"""


def count_substring(string, sub_string):
    i = count = 0
    string.sw
    while i <= len(string):
        i = string.find(sub_string, i) + 1
        if i:
            count += 1
        else:
            return count


if __name__ == '__main__':
    print(count_substring(input().strip(), input().strip()))
