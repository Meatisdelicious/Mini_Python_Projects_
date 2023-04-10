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


word1 = "sitten"
word2 = "sitting"

# To check the differences between the two strings
def diff_string(first_word,second_word):
    for caracter in range(len(first_word)) :
        # if caracter is different
        if first_word[caracter] != second_word[caracter]:
            print("nb: ", caracter)
            print(first_word[caracter]," --diff-- ",second_word[caracter] )
        # if caracter is the same
        if first_word[caracter] == second_word[caracter]:
            print("nb: ", caracter)
            print(first_word[caracter]," --same-- ",second_word[caracter] )
    return
#diff_string(word1,word2)


# return the distance between both of the string and the caracters which need to be added
def distance(word, word_to_compare_to) -> int:
    '''distance of from word1 to another word'''
    m = len(word)
    n = len(word_to_compare_to)
    count = abs(n-m)
    changes = []
    k = min(m,n)
    for i in range(k):
        # If characters are different 
        # --> add +1 to the count to know the number of changes 
        # --> append the list changes to see the difference between caracters
        if word[i] != word_to_compare_to[i]:
            count += 1
            changes.append((word[i], word_to_compare_to[i]))
        # If characters are the same --> append 0
        else:
            changes.append(0)
    # If the first word is smaller to the second
    # --> add character at the end of the first word
    if m < n:
        extra = list(word_to_compare_to[m:])
    else:
        extra = []
    return count, changes + extra
print("distance :",distance('kitten','sitting'))
print("distance :",distance('sitten','sitting'))