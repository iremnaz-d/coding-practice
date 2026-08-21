#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

neng = int(input())
english = set(map(int, input().split()))
nfra = int(input())
french = set(map(int, input().split()))
print(len(english.symmetric_difference(french)))