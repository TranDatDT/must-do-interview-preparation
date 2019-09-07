"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters
as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits
and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.

Time complexity: O(n)
"""

def run_length_encode(string: str) -> str:
    """Run length encoding
    
    Args:
        string (str): The string needs to be encoded
    
    Returns:
        str: Encoded string
    """
    count: int = 1
    previous_char: str = ''

    encode_strings: list = []

    for char in string:
        if char == previous_char:
            count += 1
        elif len(previous_char):
            encode_strings.append(f'{count}{previous_char}')
            count = 1
        previous_char = char
    
    encode_strings.append(f'{count}{previous_char}')

    return ''.join(encode_strings)


def run_length_decode(string: str) -> str:
    """Run length decoding
    
    Args:
        string (str): The string needs to be decoded
    
    Returns:
        str: Decoded string
    """
    length_index: int = 0
    char_index: int = 1
    len_string: int = len(string)

    decoded_strings: list = []

    while char_index < len_string:
        decoded_strings.append(
            f'{string[char_index] * int(string[length_index])}'
        )
        length_index += 2
        char_index += 2
    
    return ''.join(decoded_strings)

print(run_length_encode('AAAABBBCCDAA'))
print(run_length_decode('4A3B2C1D2A'))
