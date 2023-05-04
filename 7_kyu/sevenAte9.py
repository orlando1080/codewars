# Description:
# Write a function that removes every lone 9 that is inbetween 7s.

import re

def seven_ate9(str_):
    str_ = re.sub(r'(?<=7)9(?=7)', '', str_)
    return str_
