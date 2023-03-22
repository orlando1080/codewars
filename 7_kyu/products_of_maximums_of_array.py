# Task

# Given an array/list [] of integers , Find the product of the k maximal numbers.

# My Solution

def max_product(lst, n_largest_elements):
    largest = sorted(lst)[-n_largest_elements:]
    product = largest[0]
    for digit in largest[1:]:
        product *= digit
    return product
