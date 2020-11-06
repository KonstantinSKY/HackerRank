"""https://www.hackerrank.com/challenges/no-idea/problem"""

n, m = map(int, input().split())

arr = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

happy = 0
for i in arr:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1

print(happy)
