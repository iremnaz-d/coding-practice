#https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

if __name__ == '__main__':
    n = int(input())
    _list = list(input().split())
    d = Counter(_list)

    total = 0
    cnum = int(input())
    for i in range(cnum):
        shoe, price = input().split()
        if d[shoe] > 0:
            d[shoe] -= 1
            total += int(price)

    print(total)

