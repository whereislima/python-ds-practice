def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"
    phrase = phrase.lower()
    freq = {}

    for char in phrase:
        if char in vowels:
            # get(key, val), if key is not found then return val that is how the first count works
            freq[char] = freq.get(char, 0) + 1
    return freq