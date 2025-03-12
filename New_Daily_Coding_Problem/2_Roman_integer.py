class Solution(object):
    def romanToInt(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        count=0
        previous_value = 0
        for char in reversed(s) : 
            if char in roman_dict:
                value=roman_dict[char]
                if value < previous_value: 
                    count-=value
                else:
                    count+=value
                previous_value = value 
        return count

s = "III"
# Output: 3
# Explanation: III = 3.
s1 = "LIVIII"
s2 = "MCMXCIV"

sol = Solution()
print(sol.romanToInt(s))
print(sol.romanToInt(s1))
print(sol.romanToInt(s2))

