def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = ""
    other = to_swap.lower()
    for char in phrase:
        if char == to_swap or char == other:
            char = char.swapcase()
            swapped += char
        else:
            swapped += char
    return swapped