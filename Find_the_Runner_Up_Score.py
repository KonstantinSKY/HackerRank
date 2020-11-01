"""https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    for item in arr:
        if item != arr[0]:
            print(item)
            break
