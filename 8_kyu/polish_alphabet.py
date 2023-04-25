# Description:

# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
# Your task is to change the letters with diacritics:

def correct_polish_letters(st):
    return st.translate(st.maketrans('ąćęłńóśźż', 'acelnoszz'))
