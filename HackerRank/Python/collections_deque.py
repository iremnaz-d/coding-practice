#https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()

    for _ in range(n):
        args = input().split()

        if args[0] == 'append':
            d.append(int(args[1]))
        elif args[0] == 'appendleft':
            d.appendleft(int(args[1]))
        elif args[0] == 'pop':
            d.pop()
        else:
            d.popleft()
    print(*d)
