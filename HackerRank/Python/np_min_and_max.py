#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    _list = []

    for _ in range(n):
        _list.append(list(map(int, input().split())))
    print(max(np.min(np.array(_list), axis=1)))

