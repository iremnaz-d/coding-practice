#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product


def get_list():
    s = map(int, input().split())
    return s


if __name__ == '__main__':
    l1 = get_list()
    l2 = get_list()

    p_list = list(product(l1, l2))
    print(*p_list)
