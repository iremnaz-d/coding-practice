#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re

s = input()
k = input()

pattern = re.compile(rf'(?=({re.escape(k)}))')
matches = list(pattern.finditer(s))

if matches:
    for match in matches:
        print((match.start(1), match.end(1) - 1))
else:
    print((-1, -1))