#https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

def mutate_string(string, position, character):
    _list = list(string)
    _list[position] = character
    return "".join(_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)