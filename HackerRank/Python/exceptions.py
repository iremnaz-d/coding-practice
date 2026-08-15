#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

n = int(input())

for _ in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
