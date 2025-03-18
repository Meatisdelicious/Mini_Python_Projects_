class Solution(object):
    def wasa(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list=[]
        for i in range(1,n+1):
            print("i :",i)
            if i%3==0 and i%5 == 0:
                list.append("FizzBuzz")
            elif i%3 == 0: 
                list.append("Fizz")
            elif i%5 == 0:
                list.append("Buzz")
            else : 
                list.append(str(i))
        return list

n=3
n1=5
n2=15
sol=Solution()
print(sol.wasa(n))
print(sol.wasa(n1))
print(sol.wasa(n2))
