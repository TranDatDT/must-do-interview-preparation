"""
Given an array of positive integers.
Your task is to find the leaders in the array.
Note: An element of array is leader
if it is greater than or equal to all the elements to its right side.
Also, the rightmost element is always a leader.

Time complexity: O(n)
"""


from collections import deque


def find_leaders(n: int, array: list) -> deque:
    """Find leaders in an array
    
    Args:
        n (int): The size of the array
        array (list): The array
    
    Returns:
        deque: list of leaders
    """
    q: deque = deque([], n)
    
    for element in  array:
        while len(q) and element > q[-1]:
            q.pop()
        q.append(element)

    return q


def queue_to_str(q: deque) -> str:
    """Queue to string
    
    Args:
        q (dequeue): The queue
    
    Returns:
        str:
    """
    elements: list = [str(element) for element in q]
    return ' '.join(elements)


def main():
    # The number of test cases
    t: int = int(input())

    while t != 0:
        # n is the size of array
        n: int = int(input())

        # The array
        array: list = [int(number) for number in input().split()]

        leaders: deque = find_leaders(n, array)

        print(queue_to_str(leaders))

        t -= 1


if __name__ == "__main__":
    main()
