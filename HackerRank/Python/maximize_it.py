#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

import itertools

if __name__ == '__main__':
    k, m = map(int, input().split())
    _list = []

    for _ in range(k):
        l = list(map(int, input().split()))
        l.pop(0)
        _list.append(l)

    _max = 0
    for comb in itertools.product(*_list):
        _sum = sum([i**2 for i in comb])
        try_max = _sum%m
        _max = try_max if try_max>_max else _max

    print(_max)


