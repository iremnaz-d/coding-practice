#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    cnum = int(input())

    for _ in range(cnum):
        args = input().split()
        typ = args[0]
        if typ == 'remove':
            if int(args[1]) in s:
                s.remove(int(args[1]))

        elif typ == 'discard':
            s.discard(int(args[1]))

        elif typ == 'pop':
            if s:
                s.pop()

    print(sum(s))
