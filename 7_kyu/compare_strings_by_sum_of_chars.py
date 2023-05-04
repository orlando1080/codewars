# Description:

# Compare two strings by comparing the sum of their values (ASCII character code).
#
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.

def compare(st1, st2):
    if not (st1 and st1.isalpha()):
        st1 = ''
    if not (st2 and st2.isalpha()):
        st2 = ''
    return st1 == st2 if not (st1 or st2) else sum(ord(char) for char in st1.upper()) == sum(ord(char)
                                                                                             for char in st2.upper())


x, y, = 0, 1
z = 0

if z == (x and y):
    print('Yes it is')
else:
    print('No it is not')