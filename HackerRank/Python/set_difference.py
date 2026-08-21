#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

if __name__ == '__main__':
    neng = int(input())
    english = set(map(int, input().split()))
    nfra = int(input())
    french = set(map(int, input().split()))

    print(len(english.difference(french)))
