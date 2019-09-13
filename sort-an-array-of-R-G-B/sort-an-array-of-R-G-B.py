"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last.
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def sort_array(array: list) -> list:
    index_r = 0
    index_g = 0
    index_b = len(array) - 1

    while index_g <= index_b:
        if array[index_g] == 'R':
            array[index_r], array[index_g] = array[index_g], array[index_r]
            index_r += 1
        elif array[index_g] == 'G':
            index_g += 1
        else:
            array[index_g], array[index_b] = array[index_b], array[index_g]
            index_b -= 1
    
    return array


print(sort_array(['G', 'G', 'R', 'R', 'B', 'R', 'R', 'B', 'R', 'G', 'R']))
