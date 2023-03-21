# Definition
# Disarium number is the number that The sum of its digits powered with their respective positions is equal to the
# number itself.
#
# Task
# Given a number, Find if it is Disarium or not .

# My Solution
def disarium_number(number):
    return 'Disarium !!' if sum(int(digit) ** (index + 1) for index, digit in enumerate(str(number))) == number\
        else 'Not !!'