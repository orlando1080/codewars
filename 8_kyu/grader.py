# DESCRIPTION:
# Create a function that takes a number as an argument and returns a grade based on that number.

# My Solution

def grader(score):
    if 1 >= score >= 0.9:
        return 'A'
    if 0.9 > score >= 0.8:
        return 'B'
    if 0.8 > score >= 0.7:
        return 'C'
    if 0.7 > score >= 0.6:
        return 'D'
    return 'F'
