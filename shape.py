"""https://www.hackerrank.com/challenges/np-shape-reshape/problem"""

import numpy

arr = list(map(int, input().split()))
n = numpy.reshape(arr, (3, 3))
print(n)