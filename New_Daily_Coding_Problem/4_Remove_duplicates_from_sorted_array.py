# class Solution(object):
#     def wasa(self, nums):
#         nums_temp=nums
#         for i in nums_temp : 
#             print("i:",i)
#             for j in nums_temp :
#                 print("    j :",j)
#                 if i==j:
#                     removed_element=nums_temp.pop(i)
#                 continue
#         return nums
class Solution(object):
    def wasa(self, nums):
        seen=set()
        for i in range(len(nums)-1,-1,-1):
            print("i :",nums[i])
            if nums[i]in seen:
                nums.pop(i)
            else :
                seen.add(nums[i])
                print("seen :",seen)
        return len(nums)
sol=Solution()

nums = [1,1,2]
nums1 = [0,0,1,1,1,2,2,3,3,4]


# print(sol.wasa(nums))
print(sol.wasa(nums1))

