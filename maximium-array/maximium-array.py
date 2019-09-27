"""
This problem was asked by Amazon.

Given an array of numbers,
find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9],
the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""


def max_subarray(numbers):
    best_sum = 0
    best_start = best_end = 0
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end


print(max_subarray([34, -50, -100, 14, -5, 86]))
