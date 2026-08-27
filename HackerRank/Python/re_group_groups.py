#http://hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

import re

s = input()
match = re.search(r"([a-zA-Z0-9])\1", s)

print(match.group(1) if match else -1)