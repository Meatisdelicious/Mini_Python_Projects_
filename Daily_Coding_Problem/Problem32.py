# w2 6 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        res = ""
        carry = 0
        # reverse input strings
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("O") if i < len(a) else 0
            digitB = b[i] if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        # if carry is non 0
        if carry:
            res = "1" + res
        return res


sol = Solution()
print(sol.addBinary())
