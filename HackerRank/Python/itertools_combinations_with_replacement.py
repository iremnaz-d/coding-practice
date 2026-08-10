#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

from itertools import combinations_with_replacement as cwr

if __name__ == '__main__':
    s, k = input().split()
    sorted_s = "".join(sorted(s))

    _list = list(cwr(sorted_s, int(k)))
    for i in _list:
        print("".join(i))