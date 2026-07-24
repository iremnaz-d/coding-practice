#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    _list = []

    for i in range ( x +1):
        for j in range ( y +1):
            for k in range ( z +1):
                sublist = [i ,j ,k]
                _list.append(sublist)

    result = []

    for sublist in _list:
        if sum(sublist) != n:
            result.append(sublist)

    print(result)
