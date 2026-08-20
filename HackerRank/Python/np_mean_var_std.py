#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    _list = []

    for _ in range(n):
        _list.append(list(map(int, input().split())))
    array = np.array(_list)

    print(np.mean(array, axis=1), np.var(array, axis=0), round(np.std(array), 11), sep="\n")