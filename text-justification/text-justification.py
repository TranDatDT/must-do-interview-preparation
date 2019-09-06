"""
Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any,
distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
you should return the following:

["the  quick brown", # 1 extra space on the left
 "fox  jumps  over", # 2 extra spaces distributed evenly
 "the   lazy   dog"] # 3 extra spaces distributed evenly

Time complexity: O(n+n)
"""


def justify_text(words: list, k: int) -> list:
    """Justify text
    
    Args:
        words (list): list of words
        k (int): length of line
    
    Returns:
        list: Lines with justified text
    """
    # The result
    justified_text: list = []
    # Lines with not justified words
    lines: list = []
    # Count for breaking line
    count: int = 0
    # Words in a line
    temp: list = []

    for word in words:

        if count + len(temp) + len(word) <= k:
            temp.append(word)
            count += len(word)
        else:
            lines.append((temp, count))
            count = len(word)
            temp: list = [word]
    
    # Reach the last word but there is a line not added
    if len(temp):
        lines.append((temp, count))

    for line in lines:
        words: list = line[0]
        number_of_spaces: int = k - line[1]

        if len(words) == 1:
            # If line has only a word
            justified_text.append(f"{words.pop()}{' '* number_of_spaces}")
        else:
            # Number of gaps
            gap: int = len(words) - 1
            spaces_between_words: int = int(number_of_spaces / gap)
            spaces_left: int = number_of_spaces % gap

            if not spaces_left:
                justified_text.append(f"{' ' * spaces_between_words}".join(words))
            else:
                temp_words: list = []
                for index, word in enumerate(words):
                    if index <= spaces_left - 1:
                        word: str = f'{word} '
                    if index < len(words) - 1:
                        word: str = f'{word} '
                    temp_words.append(word)
                justified_text.append(''.join(temp_words))
        
    return justified_text

k = 10

words: list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

print(justify_text(words, k))
