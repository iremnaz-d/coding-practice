#https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true

# !/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


def time_delta(t1, t2):
    _format = "%a %d %b %Y %H:%M:%S %z"

    d1 = datetime.strptime(t1, _format)
    d2 = datetime.strptime(t2, _format)

    dif = d1 - d2
    return abs(int(dif.total_seconds()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
