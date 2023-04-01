# DESCRIPTION:

# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the
# even numbers at their original positions.

# My Solution

def sort_array(source_array):
    sorted_odds = sorted([n for n in source_array if n % 2 == 1])
    return [n if n % 2 == 0 else sorted_odds.pop(0) for n in source_array]
