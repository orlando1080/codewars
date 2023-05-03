# Description:

# Compare two strings by comparing the sum of their values (ASCII character code).
#
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.

def compare(st1, st2):
    if not st1 or not st1.isalpha():
        st1 = ''
    if not st2 or not st2.isalpha():
        st2 = ''
    return st1 == st2 if not st1 and not st2 else sum(ord(char) for char in st1.upper()) == sum(ord(char)
                                                                                                for char in st2.upper())
