# A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern.
# The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ...,
# where the pattern is: "add 3 to the previous term".

# In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ...
# This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".

# Your Task
# Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series
# explained above. When n < 0 return the sequence with negative terms.

def sum_of_n(n):
    if n > 0:
        return [sum(range(num + 1)) for num in range(n + 1)]
    return [sum(range(0, num - 1, -1)) for num in range(0, n - 1, -1)]

