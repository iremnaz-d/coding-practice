#https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

import re


def isValid(s):
    pattern = r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[a-zA-Z0-9]{10}$"
    return re.match(pattern, s)


if __name__ == '__main__':
    for _ in range(int(input())):
        print("Valid" if isValid(input()) else "Invalid")

