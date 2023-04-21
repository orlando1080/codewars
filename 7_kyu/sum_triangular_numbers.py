# DESCRIPTION:
# Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.
# Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation
# of the natural numbers 1, 2, 3, 4, 5, etc."

def sum_triangular_numbers(n):
    total = 0
    sum_of = 0
    for num in range(1, n + 1):
        sum_of += num
        total += sum_of
    return total