"""
Given an array C of size N-1 and given that there are numbers from 1 to N
with one element missing, the missing number is to be found.

Time complexity: O(n)
"""


def find_missing_number(n: int, array: list) -> int:
    """Find the missing number in 1-to-N array
    
    Args:
        n (int): The size of array
        array (list): The array
    
    Returns:
        int: The missing number
    """

    # Sum of 1 + 2 + 3 + ... + n
    total: int = int(n * (n + 1) / 2)

    for number in array:
        total -= number
    
    return total


def main():
    # The number of test cases
    t: int = int(input())

    while t != 0:
        # n is the size of array
        n: int = int(input())

        # The array
        array: list = [int(number) for number in input().split()]

        missing_number: int = find_missing_number(n, array)
        
        print(missing_number)

        t -= 1


if __name__ == "__main__":
    main()
