# Task
# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product
# of all the elements of Arr[] except Arr[i].

import math

def product_array(numbers):
    return [math.prod(numbers[i: ] + numbers[:i - 1]) for i in range(1, len(numbers) + 1)]
