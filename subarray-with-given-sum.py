"""
Given an unsorted array A of size N of non-negative integers,
find a continuous sub-array which adds to a given number S.

Time complexity: O(n)
"""

from collections import deque

# The number of test cases
t = int(input())

while t != 0:
    # n is the size of array
    # s is the sum
    n, s = tuple(int(_input) for _input in input().split())

    # The array
    array = [int(number) for number in input().split()]

    # Queue of elements have sum less than or equal sum 
    q = deque([], n)

    index_deque = deque([], n)

    # Sum of elements in deque q
    current_sum = 0
    
    index = 0

    found_flg = False

    while index < n:
        q.append(array[index])
        index_deque.append(index)
        current_sum += array[index]

        while len(q) and current_sum > s:
            current_sum -= q.popleft()
            index_deque.popleft()
        
        if current_sum == s:
            found_flg = True
            break

        index += 1
    
    # If reach the last element of array but subarray not found
    if not found_flg:
        while len(q) and current_sum != s:
            current_sum -= q.popleft()
            index_deque.popleft()
    
    if len(index_deque) > 1:
            print(index_deque.popleft() + 1, index_deque.pop() + 1)
    elif len(index_deque) > 0:
        final_index = index_deque.popleft() + 1
        print(final_index, final_index)
    else:
        print(-1)
    
    t -= 1
