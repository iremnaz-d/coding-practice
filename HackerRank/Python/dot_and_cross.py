#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true

import numpy

def get_matrix(n):
    _list = []
    for _ in range(n):
        _list.append(list(map(int, input().split())))
    return _list


if __name__ == '__main__':
    n = int(input())
    A = get_matrix(n)
    B = get_matrix(n)

    print(numpy.dot(A, B))

