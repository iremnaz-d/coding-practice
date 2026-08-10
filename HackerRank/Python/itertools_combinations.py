#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()
    sorted_s = "".join(sorted(s))
    _list = []

    for i in range(1, int(k) + 1):
        l = list(combinations(sorted_s, i))
        _list.extend(l)

    for i in _list:
        print("".join(i))