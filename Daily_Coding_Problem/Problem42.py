# w3 9 14. Longest Common Prefix

# Write a function to find the longest common prefix
# string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        minlen = len(strs[0])
        for i in range(1, len(strs)):
            minlen = min(minlen, len(strs[i]))
        add = ''
        for i in range(minlen):
            si = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != si:
                    return add
            add += si
        return add


strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
sol = Solution()
print(sol.longestCommonPrefix(strs1))
