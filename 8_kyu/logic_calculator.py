# Your Task
# Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the
# operator to the values in the array.

def logical_calc(array, op):
    return eval(f' {"^" if op == "XOR" else op.lower()} '.join(str(bool) for bool in array))