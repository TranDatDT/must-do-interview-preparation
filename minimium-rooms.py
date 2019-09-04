"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end)
for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

Time Complexity: O(n) * log(n)
"""

from collections import deque

# Time intervals
intervals = [(5, 6), (5, 10), (7, 8), (8, 16), (10, 30), (15, 20)]

# O(n) * log(n)
sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

cnt = 0

d = deque([], maxlen=len(intervals))

for it in sorted_intervals:
    start, end = it[0], it[1]

    while len(d) and d[0] <= start:
        d.popleft()
    
    d.append(end)

    if len(d) > cnt:
        cnt = len(d)

print(cnt)
