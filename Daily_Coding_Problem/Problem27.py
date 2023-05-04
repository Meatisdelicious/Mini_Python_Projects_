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
        temp = []
        for char_r in ransomNote:
            for char_m in magazine :
                if char_r in char_m:
                    temp.append(char_r)
                    print(temp)
                    if len(temp) == len(ransomNote):
                        return True
                else :
                    return False
    
sol = Solution()
ransomNote1="a"
magazine1="b"
print(sol.canConstruct(ransomNote1,magazine1))
ransomNote1="aa"
magazine1="ab"
print(sol.canConstruct(ransomNote1,magazine1))
ransomNote2="aa"
magazine2="aab"
print(sol.canConstruct(ransomNote2,magazine2))       
