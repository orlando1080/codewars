# DESCRIPTION:
# Longest Palindrome
# Find the length of the longest substring in the given string s that is the same in reverse.

# As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

# If the length of the input string is 0, the return value must be 0.

def longest_palindrome(s):
        longest_palidrome = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                check = s[i: j + 1]
                if check == check[::-1] and len(check) > longest_palidrome:
                    longest_palidrome = len(check)
                else:
                    continue
        return longest_palidrome
