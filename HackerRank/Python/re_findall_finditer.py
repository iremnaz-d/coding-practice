#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re

if __name__ == '__main__':
    s = input()
    vowels = "aeiou"
    consonants = "qwrtypsdfghjklzxcvbnm"

    pattern = rf"(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])"

    matches = re.findall(pattern, s, flags=re.I)

    if matches:
        print("\n".join(matches))
    else:
        print(-1)

