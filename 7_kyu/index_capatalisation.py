# DESCRIPTION:
# Given a string and an array of integers representing indices, capitalize all letters at the given indices.

def capitalize(s, ind):
    return ''.join(char.upper() if index in ind else char for index, char in enumerate(s))