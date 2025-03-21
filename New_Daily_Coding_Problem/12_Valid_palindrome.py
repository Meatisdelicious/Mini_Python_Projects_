import re
class Solution(object):
    def wasa(self, s):
        # s_clean = s.replace(",", "").replace(":", "").replace(" ","").lower()
        s_clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print("string with no spaces :",s_clean)
        string_length = len(s_clean)
        print("len(s)",string_length)
        for i in range(string_length//2):
            print(f"Comparing: {s_clean[i]} vs {s_clean[string_length - 1 - i]}")
            if s_clean[i]!=s_clean[string_length-1-i]:
                print("the compared strings are not the same")
                return False
        return True

s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s2 = " "
sol = Solution()
print(sol.wasa(s))
print(sol.wasa(s1))
print(sol.wasa(s2))