#https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

from itertools import groupby

if __name__ == '__main__':
    l = list(input())

    for k, g in groupby(l):
        count = len(list(g))
        print((count, int(k)), end = " ")