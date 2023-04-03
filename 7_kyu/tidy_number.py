# DESCRIPTION:

# Definition
# A Tidy number is a number whose digits are in non-decreasing order.

# Task
# Given a number, Find if it is Tidy or not .

def tidyNumber(n):
    number = str(n)
    for index in range(1, len(number)):
        if number[index] < number[index - 1]:
            return False
    return True
