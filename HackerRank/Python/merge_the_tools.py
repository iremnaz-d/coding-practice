#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    num = int(len(string) / k)
    _list = []
    index = 0
    for i in range(num):
        _list.append(string[index:index + k])
        index += k

    for i in _list:
        print("".join(dict.fromkeys(i)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)