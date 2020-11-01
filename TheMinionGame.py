"""https://www.hackerrank.com/challenges/the-minion-game/problem"""


def minion_game(string):
    stuart = kevin = 0
    vowels = 'AEIOU'
    len_str = len(string)

    for x in range(len_str):
        if string[x] in vowels:
            kevin += (len_str-x)
        else:
            stuart += (len_str-x)

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    minion_game(input())
