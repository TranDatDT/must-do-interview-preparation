"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of
character insertions, deletions, and substitutions required to
change one string to the other. For example, the edit distance between
“kitten” and “sitting” is three: substitute the “k” for “s”,
substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

Time complexity: O(n+m) + O(n*m)

Reference: https://en.wikipedia.org/wiki/Levenshtein_distance
"""


def caculate_levenshtein_distance(s: str, t: str) -> int:
    """Caculate Levenshtein distance between 2 strings
    
    Arguments:
        s {str} -- First string
        t {str} -- Second string
    
    Returns:
        int -- Levenshtein distance
    """
    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(1, rows):
        dist[i][0] = i

    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution
 
    return dist[row][col]


print(caculate_levenshtein_distance("kitten", "sitting"))
