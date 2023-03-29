# DESCRIPTION:
# Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace
# all the rotten pieces of fruit with fresh ones. For example, given ["apple","rottenBanana","apple"] the replaced array
# should be ["apple","banana","apple"]. Your task is to implement a method that accepts an array of strings containing
# fruits should returns an array of strings where all the rotten fruits are replaced by good ones.

# My Solution
def remove_rotten(bag_of_fruits):
    if bag_of_fruits is None:
        return []
    return [fruit[6:].lower() if fruit.startswith('rotten') else fruit for fruit in bag_of_fruits]