"""https://www.hackerrank.com/challenges/designer-door-mat/problem"""

def print_door_mat(size):
    n, m = map(int, size.split())

    middle_str = "WELCOME".center(m, "-")
    picture_str = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print("\n".join(picture_str))
    print(middle_str)
    print("\n".join(picture_str[::-1]))


if __name__ == '__main__':
    print_door_mat(input())




















































