#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

from collections import OrderedDict

if __name__ == '__main__':
    s = input()
    d = OrderedDict()

    for i in list(s):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    d_vals = OrderedDict(sorted(d.items(), key= lambda x: (-x[1], x[0])))

    cnt = 0
    for k,v in d_vals.items():
        print(k, v)
        cnt += 1
        if cnt >2: break
