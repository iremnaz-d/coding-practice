#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

s = list(input())
s.sort(key=lambda x: (
    x.isdigit(),
    x.isdigit() and int(x) % 2 == 0,
    x.isupper(),
    x
))

print("".join(s))
