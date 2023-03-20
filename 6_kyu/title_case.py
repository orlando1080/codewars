# DESCRIPTION:
# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the
# first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case
# unless it is the first word, which is always capitalised.
# Write a function that will convert a string into title case, given an optional list of exceptions (minor words).
# The list of minor words will be given as a string with each word separated by a space.
# Your function should ignore the case of the minor words string -- it should behave in the same way even if the case
# of the minor word string is changed.

# My solution

def title_case(title, minor_words=''):
    if title:
        minor_words = [word.lower() for word in minor_words.split()]
        words = title.split()
        words[0] = words[0].title()
        title_case_words = [word.title() if word.lower() not in minor_words else word.lower() for word in words[1:]]

        return ' '.join([words[0]] + title_case_words)
    return title