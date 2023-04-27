# Description:

# Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return
# undefined/None/nil/NULL if any of the values aren't numbers.
# Note: Booleans should not be considered as numbers.

def cube_odd(arr):
    return None if not isinstance(arr, list) or any(type(n) != int for n in arr) else sum(n ** 3 for n in arr if n % 2)
