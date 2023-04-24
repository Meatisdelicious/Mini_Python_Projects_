# 7 Valid anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# stypically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


def valid_anagram(string1, string2):
    if len(string1) != len(string2):
        return False

    string_to_list1 = list(string2)
    for element in string1:
        if element in string_to_list1:
            temp = string_to_list1.index(element)
            string_to_list1.pop(temp)
            if len(string_to_list1) == 0:
                return True
        else:
            return False


s = "anagram"
t = "nagaram"
s1 = "rat"
t1 = "car"

print(valid_anagram(s, t))
print(valid_anagram(s1, t1))


# optimised version :
# def isAnagram(self, s: str, t: str) -> bool:
#     return all(s.count(x) == t.count(x) for x in string.ascii_lowercase)
