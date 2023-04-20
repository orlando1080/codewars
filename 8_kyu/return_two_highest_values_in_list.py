# Description

# In this kata, your job is to return the two distinct highest values in a list. If there are less than 2 unique values,
# return as many of them, as possible.
# The result should also be ordered from highest to lowest.

def two_highest(arg1):
    return sorted(list(set(arg1)))[-2:][::-1]
