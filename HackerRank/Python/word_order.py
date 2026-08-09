#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())

    dictionary = {}
    for _ in range(n):
        s = input()
        if s in dictionary:
            dictionary[s] += 1
        else:
            dictionary[s] = 1

    print(len(dictionary))
    for i in dictionary.values():
        print(i, end=" ")
