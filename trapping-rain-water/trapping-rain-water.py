"""
This problem was asked by Facebook.

You are given an array of non-negative integers
that represents a two-dimensional elevation map
where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map
in O(N) time and O(1) space.

For example, given the input [2, 1, 2],
we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5],
we can hold 3 units in the first index, 2 in the second,
and 3 in the fourth index
(we cannot hold 5 since it would run off to the left),
so we can trap 8 units of water.
"""


def trap_rain_water(walls: list) -> int:
    """Count units of trapped water
    Start with the highest wall is the leftmost or rightmost one.
    If the current wall is higher than the highest previous wall,
    update the highest wall with the current one.
    If not, calculate the difference between the highest and the current.
    The result is the sum of all the differences.

    Args:
        walls (list): The list of walss
    
    Returns:
        int: The units of trapped water
    """
    # Number of walls in array
    len_walls: int = len(walls)

    # The result
    trapped_units: int = 0

    # Highest wall
    max_height: int = 0

    # Leftmost wall
    left_height: int = walls[0]

    # Rightmost wall
    right_height: int = walls[-1]

    # If the leftmost wall is smaller than the rightmost wall
    # we start from left to right
    if left_height <= right_height:
        for wall in walls:
            if wall > max_height:
                max_height = wall
            else:
                trapped_units += max_height - wall
    # otherwise we start from right to left
    else:
        for wall_index in range(len_walls - 1, -1, -1):
            if walls[wall_index] > max_height:
                max_height = walls[wall_index]
            else:
                trapped_units += max_height - walls[wall_index]

    return trapped_units


print(trap_rain_water([3, 0, 0, 2, 4]))
