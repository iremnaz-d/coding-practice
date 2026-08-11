#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())

    d = OrderedDict()
    for _ in range(n):
        args = input().split()
        price = int(args[-1])
        args.pop()
        name = " ".join(args)

        if name in d:
            d[name] += price
        else:
            d[name] = price
    print("\n".join([f"{key} {value}" for key, value in d.items()]))
