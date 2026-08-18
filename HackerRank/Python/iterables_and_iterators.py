#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations

if __name__ == '__main__':
    length = int(input())
    s = list(input().split())
    index = int(input())

    combs = list(combinations(s,index))
    count = 0
    count += sum([1 if 'a' in i else 0 for i in combs])
    print(f"{count/len(combs):.4f}")