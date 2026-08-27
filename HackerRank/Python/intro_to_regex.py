#https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

for _ in range(int(input())):
    s = input()
    l = list(s)
    if l[0] not in ["+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        print(False)
        continue

    cnt = 0
    for i in l:
        if i == ".":
            cnt += 1

    if cnt != 1:
        print(False)
        continue

    try:
        float(s)
        print(True)
        continue
    except Exception:
        print(False)
        continue