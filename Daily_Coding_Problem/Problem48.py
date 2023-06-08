# w4 3 9. Palindrome Number

# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.


# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            print("true")
            return True
        else:
            print("false")

            return False


x1 = 121
x2 = -121
x3 = 10

sol = Solution()
sol.isPalindrome(x1)
sol.isPalindrome(x2)
sol.isPalindrome(x3)
