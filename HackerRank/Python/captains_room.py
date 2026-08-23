#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))
room_counts = Counter(rooms)
min_tuple = min(room_counts.items(), key = lambda x: x[1])
print(min_tuple[0])