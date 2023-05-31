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
        result = []
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                common_elements = list(set(strs[i]) & set(strs[j]))
                result.extend(common_elements)
        return result


strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
sol = Solution()
print(sol.longestCommonPrefix(strs2))
