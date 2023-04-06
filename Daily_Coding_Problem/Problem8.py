# Problem #31

# This problem was asked by Google.

# The edit distance between two strings refers to
# the minimum number of character insertions,
# deletions, and substitutions required to change one
# string to the other.
# For example, the edit distance between “kitten” and
# “sitting” is three:
# substitute the “k” for “s”, substitute the “e” for “i”,
# and append a “g”.
# Given two strings, compute the edit distance between them


word1 = "kitten"
word2 = "sitting"

def check_equal_strings(word,word_to_compare_to):
    if word1==word2:
        print("both words are equal")
    else :
        print("strings are not equal")
    return
# check_equal_strings(word1,word2)

for caracter in range(len(word1)) :
    print(caracter)
    if word1[caracter] != word2[caracter]:
        print("not equal")
        break
else : 
    print("equal")
