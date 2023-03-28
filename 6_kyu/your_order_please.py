# DESCRIPTION:
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position
# the word should have in the result.

# My solution

def order(sentence):
    return ' '.join(word for index in range(len(sentence)) for word in sentence.split() if str(index + 1) in word)
