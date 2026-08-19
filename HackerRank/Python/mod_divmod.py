#https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true

if __name__ == '__main__':
    a, b = int(input()), int(input())
    print(a//b, a%b, divmod(a,b), sep = "\n")