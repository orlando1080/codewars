# DESCRIPTION:
# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
#
# For each word:
#
# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces

# My solution
import re


def decipher_this(s):
    decipher = []
    numbers = re.findall(r'\d+', s)
    for num in numbers:
        s = s.replace(num, chr(int(num)))
    words = s.split()
    for word in words:
        if len(word) > 2:
            word = list(word)
            word[1], word[-1] = word[-1], word[1]
            word = ''.join(word)
            decipher.append(word)
        else:
            decipher.append(word)
    return ' '.join(decipher)