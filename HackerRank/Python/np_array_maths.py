#https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy as np

n, m = map(int, input().split())

list_A = [list(map(int, input().split())) for _ in range(n)]
list_B = [list(map(int, input().split())) for _ in range(n)]

A = np.array(list_A)
B = np.array(list_B)

print(np.add(A, B), np.subtract(A, B), np.multiply(A, B), np.floor_divide(A, B), np.mod(A, B), np.power(A, B), sep="\n")