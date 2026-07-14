#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true


from collections import defaultdict


def create_group(d, n, name):
    for i in range(n):
        element = input()
        d[name].append(element)


if __name__ == "__main__":

    n, m = map(int, input().split())

    d = defaultdict(list)
    create_group(d, n, "A")
    create_group(d, m, "B")

    for valB in d["B"]:
        positions = []
        for index, valA in enumerate(d["A"]):
            if valB == valA:
                positions.append(str(index + 1))

        if positions:
            for p in positions:
                print(p, end=" ")
        else:
            print("-1")
        print()




