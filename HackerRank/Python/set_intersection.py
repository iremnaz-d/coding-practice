#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

enum = int(input())
english = set(map(int, input().split()))
fnum = int(input())
french = set(map(int, input().split()))

print(len(english.intersection(french)))