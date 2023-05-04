# Description:
# Write a function that removes every lone 9 that is inbetween 7s.

import re

import re

def seven_ate9(str_):
    return re.sub(r'(?<=7)9(?=7)', '', str_)
