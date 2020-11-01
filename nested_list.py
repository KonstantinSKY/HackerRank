"""https://www.hackerrank.com/challenges/nested-list/problem"""

if __name__ == '__main__':
    grade_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_list.append([name, score])

    grade_list.sort(key=lambda x: x[1])
    second_grades = []

    for i in range(1, len(grade_list)):
        if grade_list[i][1] == grade_list[0][1]:
            continue
        if not second_grades or second_grades[0][1] == grade_list[i][1]:
            second_grades.append(grade_list[i])
            continue
        break

    [print(second_grade[0]) for second_grade in sorted(second_grades, key=lambda x: x[0])]

    # for HackerRank
    # for second_grade in sorted(second_grades, key=lambda x: x[0]):
    #     print(second_grade[0])
