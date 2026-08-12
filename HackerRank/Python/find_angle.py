#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true


import math
if __name__ == '__main__':
    b, a = int(input()), int(input())
    angle = round(math.degrees(math.atan2(b, a)))
    print(angle, chr(176), sep="")