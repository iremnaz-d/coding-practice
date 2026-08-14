#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

if __name__ == '__main__':
    m, set1 = int(input()), set(map(int, input().split()))
    n, set2 = int(input()), set(map(int, input().split()))

    dif1 = set1.difference(set2)
    dif2 = set2.difference(set1)
    result = sorted(list(dif1.union(dif2)))

    print(*result, sep="\n")