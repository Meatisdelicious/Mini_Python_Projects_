# class Solution(object):
#     def wasa(self, nums):
#         seen=set()
#         for i in range(len(nums)-1,-1,-1):
#             print("i :",nums[i])
#             if nums[i]in seen:
#                 nums.pop(i)
#             else :
#                 seen.add(nums[i])
#                 # print("seen :",seen)
#         return seen

from collections import Counter
class Solution(object):
    def wasa(self, nums):
        # Count how many times each number appears in nums
        num_counts = Counter(nums)
        print("num_counts :",num_counts)
        # Return a set containing only the numbers that appear exactly once
        unique_number=0
        for num in nums :
            print("num :",num)
            if num_counts[num]==1:
                return num                      

    
sol=Solution()

nums = [2,2,1]
nums1 = [4,1,2,1,2]
nums2 = [1]
print(sol.wasa(nums1))