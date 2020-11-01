"""https://www.hackerrank.com/challenges/merge-the-tools/problem"""


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        line = string[i:i+k]
        print(''.join(sorted(set(line), key=line.index)))


if __name__ == '__main__':
    merge_the_tools(input(), int(input()))
