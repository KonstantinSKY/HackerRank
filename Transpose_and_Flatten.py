"""https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem"""

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))

    my_arr = numpy.array(arr)
    print(numpy.transpose(my_arr))
    print(my_arr.flatten())
