#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    _list = []

    for _ in range(N):
        args = input().split()
        command = args[0]

        if command == 'insert':
            _list.insert(int(args[1]), int(args[2]))
        elif command == 'print':
            print(_list)
        elif command == 'remove':
            _list.remove(int(args[1]))
        elif command == 'append':
            _list.append(int(args[1]))
        elif command == 'sort':
            _list.sort()
        elif command == 'pop':
            _list.pop()
        else:
            _list.reverse()

