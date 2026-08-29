#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x ** 3


def fibonacci(n):
    l = [0, 1]
    if n == 1:
        return [0]
    elif n <= 0:
        return []

    for i in range(n):
        if i != 0 and i != 1:
            l.append(l[i - 2] + l[i - 1])
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))