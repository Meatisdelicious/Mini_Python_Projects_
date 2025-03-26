class Solution(object):
    def wasa(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp_list=[]
        for word in strs:
            print(word)
            for i in range(len(word)):
                print(word[i])
            # for i in range(len(word)):
            # for letter in word:
            #     temp_list+=letter
            #     if temp_list=

                # print(i)

        return
    
strs = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]

sol=Solution()
print(sol.wasa(strs))