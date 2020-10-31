"""https://www.hackerrank.com/challenges/finding-the-percentage/problem"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    print('{:.2f}'.format(sum(marks) / len(marks)))
