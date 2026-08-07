#https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1,n+1):
        _dec = str(i).rjust(width)
        _oct = oct(i)[2:].rjust(width)
        _hex = hex(i)[2:].upper().rjust(width)
        _bin = bin(i)[2:].rjust(width)
        print(_dec,_oct,_hex,_bin)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)