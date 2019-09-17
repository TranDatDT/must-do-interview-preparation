"""
This problem was asked by Google.

The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3},
it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

Time complexity: O(2^n - 2)
"""


def generate_power_set(li: list) -> list:
    """Generates power set of a set
    
    Arguments:
        li {list} -- the set want to generate its power set
    
    Returns:
        list -- the power set
    """
    f_subset: list = [[], [li.pop()]]

    while len(li):
        element: int = li.pop()
        temp: list = f_subset[:]

        for subset in temp:
            subset_copy: list = subset[:]
            subset_copy.append(element)
            f_subset.append(subset_copy)

    return f_subset

print(generate_power_set([1, 2, 3, 4, 5]))
