"""
Given an array of positive integers.
Your task is to find the leaders in the array.
Note: An element of array is leader
if it is greater than or equal to all the elements to its right side.
Also, the rightmost element is always a leader.

Time complexity: O(n)
"""


def find_leaders(n: int, array: list) -> list:
    """Find leaders in an array
    
    Args:
        n (int): The size of the array
        array (list): The array
    
    Returns:
        list: list of leaders
    """
    leaders: list = []
    max_from_right: int = array[-1]
    leaders.append(max_from_right)

    for index in range(n - 2, -1, -1):
        if max_from_right <= array[index]:
            max_from_right = array[index]
            leaders.append(max_from_right)
    
    return leaders


def main():
    # The number of test cases
    t: int = int(input())

    while t != 0:
        # n is the size of array
        n: int = int(input())

        # The array
        array: list = [int(number) for number in input().split()]

        leaders: list = find_leaders(n, array)

        while len(leaders):
            print(leaders.pop(), end=" ")

        t -= 1


if __name__ == "__main__":
    main()
