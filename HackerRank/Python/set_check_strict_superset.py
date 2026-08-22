#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

A = set(map(int, input().split()))
flag = False

for _ in range(int(input())):
    B = set(map(int,input().split()))
    if len(A.difference(B)) > 0 and len(B.difference(A)) == 0:
        flag = True
    else:
        flag = False
        break

print(flag)
