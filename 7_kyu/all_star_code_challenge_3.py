# Description:

# Create a function, called removeVowels (or remove_vowels), that takes a string argument and returns that same string
# with all vowels removed (vowels are "a", "e", "i", "o", "u").

import re

def remove_vowels(strng: str):
    return re.sub(r'[aeiou]', '', strng)
