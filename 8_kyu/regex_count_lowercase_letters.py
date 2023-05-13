# Description:
# Your task is simply to count the total number of lowercase letters in a string.

import re


def lowercase_count(strng):
    return len(re.findall(r'[a-z]', strng))
