"""
Given an array of distinct integers.
The task is to count all the triplets such that
sum of two elements equals the third element.

Time complexity: O(n^2)
"""


def count_the_triplets(n: int, array: list) -> int:
    """Count the triplets
    
    Args:
        n (int): The size of array
        array (list): The array
    
    Returns:
        int: The number of triplets. Return -1 if there is no triplets.
    """
    # Hash table
    hash_table: set = set(array)

    # The number of triplets
    count: int = 0

    for index_1 in range(0, n - 1):
        for index_2 in range(index_1 + 1, n):
            if array[index_1] + array[index_2] in hash_table:
                count += 1
    
    if count:
        return count
    else:
        return -1


def main():
    # The number of test cases
    t: int = int(input())

    while t != 0:
        # n is the size of array
        n: int = int(input())

        # The array
        array: list = [int(number) for number in input().split()]

        count: int = count_the_triplets(n, array)

        print(count)

        t -= 1


if __name__ == "__main__":
    main()
