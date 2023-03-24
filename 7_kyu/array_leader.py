# Definition
# An element is leader if it is greater than The Sum all the elements to its right side.

# Task
# Given an array/list [] of integers , Find all the LEADERS in the array.

# My solution

def array_leaders(numbers):
    running_sum = 0
    leaders = []
    for number in numbers[::-1]:
        if number > running_sum:
            leaders.append(number)
            running_sum += number
        else:
            running_sum += number
    return leaders[::-1]
