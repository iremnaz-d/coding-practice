#https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(_line):
    _list = _line.split(" ")
    return "-".join(_list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)