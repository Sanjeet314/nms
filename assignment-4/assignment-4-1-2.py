"""
1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
"""
def filter_long_words(bagOfWords, n):
    biggerThanN = []
    for i in bagOfWords:
        if(len(i) > n):
            biggerThanN.append(i)

    return biggerThanN

n = int(input("Enter n: "))
print(filter_long_words(['Hi', 'Lois', 'Hi', 'Peter'], n))
