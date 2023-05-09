# Complete the solution so that it returns a formatted string. The return value should equal "Value is VALUE"
# where value is a 5 digit padded number.

def solution(value):
    return f'Value is {str(value).zfill(5)}'

# No method solution.
def solution2(value):
    return f'Value is {"0" * (5 - len(str(value)))}{str(value)}'
