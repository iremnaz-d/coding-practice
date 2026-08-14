#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

if __name__ == '__main__':
    n , m= map(int, input().split())
    array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    happiness = 0
    happiness += sum([i in A  for i in array]) - sum([i in B for i in array])
    print(happiness)




