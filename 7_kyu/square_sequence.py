# Description
# Complete the function that returns an array of length n, starting with the given number x and the squares of the
# previous number. If n is negative or zero, return an empty array/list.

def squares(x, n):
    if n <= 0:
        return []
    prod = x
    seq = [x]
    for i in range(n - 1):
        prod **= 2
        seq.append(prod)
    return seq
