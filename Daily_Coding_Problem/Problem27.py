# w2 2 383. Ransom Note


# Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true


class Solution(object):
    def canConstruct(self, ransomNote, magazine):

    
sol = Solution()

ransomNote="a"
magazine="b"
print(sol.canConstruct(ransomNote,magazine))
ransomNote1="aa"
magazine1="ab"
print(sol.canConstruct(ransomNote1,magazine1))
ransomNote2="aa"
magazine2="aab"
print(sol.canConstruct(ransomNote2,magazine2))
ransomNote3="aab"
magazine3="baa"
print(sol.canConstruct(ransomNote3,magazine3))      
