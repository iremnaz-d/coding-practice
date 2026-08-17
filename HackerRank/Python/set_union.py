#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

enum = int(input())
english = set(map(int, input().split()))
fnum = int(input())
french = set(map(int, input().split()))

print(len(english.union(french)))