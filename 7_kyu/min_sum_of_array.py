# Task
# Given an array of integers, Find the minimum sum which is obtained from summing each Two integers product.

def min_sum(arr):
    return sum(sorted(arr)[index] * sorted(arr)[len(arr) - 1 - index] for index in range(len(arr) // 2))