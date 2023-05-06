# Description:

# Given two words and a letter, return a single word that's a combination of both words, merged at the point where the
# given letter first appears in each word. The returned word should have the beginning of the first word and the ending
# of the second, with the dividing letter in the middle. You can assume both words will contain the dividing letter.


def string_merge(string1, string2, letter):
    return f'{string1.split(letter, 1)[0]}{letter}{string2.split(letter, 1)[-1]}'
