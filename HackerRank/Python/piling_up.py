#https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

def isPile(l):
    left = 0
    right = len(l) - 1
    max_num = float('inf')

    while True:
        right_num = l[right]
        left_num = l[left]

        if right == left and right_num <= max_num:
            return "Yes"

        if right_num >= left_num and right_num <= max_num:
            max_num = right_num
            right -= 1
        elif left_num > right_num and left_num <= max_num:
            max_num = left_num
            left += 1
        else:
            return "No"


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        size = int(input())
        l = list(map(int, input().split()))

        print(isPile(l))
