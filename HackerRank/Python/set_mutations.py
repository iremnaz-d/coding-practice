#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

n = int(input())
A = set(map(int, input().split()))

loop = int(input())
for _ in range(loop):
    args = input().split()
    op = args[0]
    B = set(map(int, input().split()))

    if op == 'update':
        A.update(B)
    elif op == 'intersection_update':
        A.intersection_update(B)
    elif op == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    else:
        A.difference_update(B)

print(sum(A))

