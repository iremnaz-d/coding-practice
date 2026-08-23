#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

for _ in range(int(input())):
    input()
    A = set(map(int, input().split()))
    input()
    B = set(map(int, input().split()))
    print(len(A.difference(B)) == 0)