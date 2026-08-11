#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

from collections import namedtuple

# 1st solution
if __name__ == '__main__':
    snum = int(input())

    _list = input().split()
    index = _list.index('MARKS')
    _sum = 0
    for i in range(snum):
        l = input().split()
        _sum += int(l[index])

    print(_sum / snum)


# 2nd solution
if __name__ == '__main__':
    n, Student = int(input()), namedtuple('Student', input())
    notes = [int(Student(*input().split()).MARKS) for _ in range(n)]
    print(sum(notes)/n)


