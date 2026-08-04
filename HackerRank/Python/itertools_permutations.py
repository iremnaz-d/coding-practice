#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations

if __name__ == '__main__':
    args = input().split()
    _list = list(args[0])
    _list.sort()

    p_list = []

    if len(args) == 1:
        p_list = list(permutations(_list))
    else:
        p_list = list(permutations(_list, int(args[1])))

    for i in p_list:
        print("".join(i))