class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # Take the first string as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                # If current index is out of range or character doesn't match
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]

    
strs = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]

sol=Solution()
print(sol.longestCommonPrefix(strs))