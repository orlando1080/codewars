# Description:

# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers,
# and return the result in %.

# Example:

# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.

def compare(a, b):
    return '100%' if sorted(str(a)) == sorted(str(b)) else '50%' if str(a)[0] in str(b) or str(a)[1] in str(b) else '0%'
