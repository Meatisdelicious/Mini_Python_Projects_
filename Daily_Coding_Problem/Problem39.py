# w3 6 338. Counting Bits   (6 bcs some were skipped)

# Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is the number
# of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

class Solution(object):
    def countBits(self, n):
        output = [0]
        while (len(output) <= n):
            output.extend([i+1 for i in output])
        return output[:n+1]


sol = Solution()
n = 2
n1 = 5
print(sol.countBits(n1))
