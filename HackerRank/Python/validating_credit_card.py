#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true

import re


def isValid(s):
    pattern = r"^[456]\d{3}(-?\d{4}){3}$"
    if re.match(pattern, s):

        if "-" in s:
            l = s.split("-")
            if any(len(i) != 4 or i == " " or not i.isdigit() for i in l):
                return False

        clean_s = s.replace("-", "")
        if re.search(r"(\d)\1{3}", clean_s):
            return False

        return True
    return False


if __name__ == '__main__':
    for _ in range(int(input())):
        print("Valid" if isValid(input()) else "Invalid")