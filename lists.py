"""https://www.hackerrank.com/challenges/python-lists/problem"""

if __name__ == '__main__':
    N = int(input())
    list_ = []
    command_list = [input().split() for i in range(N)]
    for command in command_list:
        if command[0] == 'print':
            print(list_)
            continue

        arguments = ",".join(command[1:])
        eval(f"list_.{command[0]}({arguments})")

        # for HackerRank
        # use raw_input()
        # eval("list_." + command[0] + "(" + arguments + ")")
