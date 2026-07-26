#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    _list = list(arr)

    _list.sort(reverse = True)
    first = _list[0]

    for i in _list:
        if first != i:
            print(i)
            break
