# Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

def explode(s):
    return ''.join(digit * int(digit) for digit in s)

