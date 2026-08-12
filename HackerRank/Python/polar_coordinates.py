#https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

from cmath import polar

if __name__ == '__main__':
    num = complex(input())
    cnum = polar(num)
    print(cnum[0])
    print(cnum[1])