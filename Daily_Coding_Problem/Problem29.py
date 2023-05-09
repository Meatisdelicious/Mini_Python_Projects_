# w2 4 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
# adding comment

class Solution(object):
    def longestPalindrome(self, s):
        letters = {}
        # converts string to dictionary
        for char in s:
            # if it's not in our dictionary--> add it
            if char not in letters:
                letters[char] = 1
            # if it is...
            else:
                letters[char] += 1
        result = 0
        odd_numbers = 0
        # if there is just one time, one character in the entire string
        if len(letters) == 1:
            return letters[s[0]]

        for i in letters.values():
            print(i)
            # checking if there is more than one character
            if i > 1:
                if i % 2 == 0:
                    result += i
                else:
                    result += i-1
                    odd_numbers += 1
            else:
                odd_numbers += 1
        # adding an odd value to the result, bcs according to the theory, we can. (to be symetrical)
        if odd_numbers > 0:
            result += 1
        return result


sol = Solution()
s = "abccccdd"
s1 = "a"
sol.longestPalindrome(s)
