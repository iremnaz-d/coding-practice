#https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

n, x = map(int, input().split())
_list = []

for _ in range(x):
    _list.append(list(map(float, input().split())))

grades = zip(*_list)

for i in grades:
    print(sum(i) / x)
