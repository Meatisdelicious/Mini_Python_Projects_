class Solution(object):
    def wasa(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        last_word=words[-1]
        last_word_str = str(last_word)
        count=0
        for letter in last_word_str:
            print(letter)
            count+=1
        return count
    
s = "Hello World"
s1 = "   fly me   to   the moon  " 
s2 = "luffy is still joyboy"
sol=Solution()
print(sol.wasa(s))
print(sol.wasa(s1))
print(sol.wasa(s2))