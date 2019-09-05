"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

Time complexity: O(n)
"""


def is_balanced(string: str) -> bool:
    """Check whether the brackets are balanced
    
    Args:
        string (str): string of brackets
    
    Returns:
        bool: True if balanced, otherwise False
    """

    open_brackets = {'(', '{', '['}
    close_brackets = {')', '}', ']'}
    bracket_pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    stack = []

    for bracket in string:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if len(stack) and bracket_pairs[bracket] == stack[-1]:
                stack.pop()
            else:
                return False

    if not len(stack):
        return True
    
    return False


string = '([)]'
print(is_balanced(string))
