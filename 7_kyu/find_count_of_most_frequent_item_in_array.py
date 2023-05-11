# Description:
# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array
# of integers. For an empty array return 0

def most_frequent_item_count(collection):
    return max(collection.count(x) for x in collection) if collection else 0
