"""
2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
"""


def trueVowel(char):
    if char in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False


user_input = input('Enter Your Character\n')[0].lower()
print(trueVowel(user_input))
