#https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true

#with Python 2

import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if not s:
            print("False")
            continue

        try:
            re.compile(s)
            print("True")
        except Exception:
            print("False")

