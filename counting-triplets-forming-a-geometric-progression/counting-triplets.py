"""
https://www.hackerrank.com/challenges/count-triplets-1
"""

from collections import defaultdict


def countTriplets(arr, r):
    total = 0
    single, double = defaultdict(int), defaultdict(int)
    for a in arr:
        if a % r == 0:
            total += double[a//r]
            double[a] += single[a//r]
        single[a] += 1
    return total
