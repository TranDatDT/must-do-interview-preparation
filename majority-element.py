"""
Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N is an element
that appears more than N/2 times in the array.
"""


def find_majority_element(n: int, array: list) -> int:
    """Find the majority element of an array
    
    Args:
        n (int): The size of array
        array (list): The array
    
    Returns:
        int: The majority element. Return -1 if not found.
    """

    # N/2
    half_of_n: int = int(n / 2)

    # Count of each element
    elements_count: dict = {}

    # Majority element
    majority_element: int = -1

    # Greatest count for choosing only one majority element
    greatest_count: int = 0

    for element in array:
        if element in elements_count:
            elements_count[element] += 1
        else:
            elements_count[element] = 1
        
        if (elements_count[element] > half_of_n and
            elements_count[element] > greatest_count):
            majority_element = element
            greatest_count = elements_count[element]
    
    return majority_element


def main():
    # The number of test cases
    t: int = int(input())

    while t != 0:
        # n is the size of array
        n: int = int(input())

        # The array
        array: list = [int(number) for number in input().split()]

        majority_element: int = find_majority_element(n, array)

        print(majority_element)

        t -= 1


if __name__ == "__main__":
    main()
