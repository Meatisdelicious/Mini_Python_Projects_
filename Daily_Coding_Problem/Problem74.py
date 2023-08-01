# w8 525. Contiguous Array


# Given a binary array nums, return the maximum length of a 
# contiguous subarray with an equal number of 0 and 1.

# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, nums):
        seen_at ={}
        seen_at[0]=-1
        ans = count = 0
        # enumerate is used to get the index and the value at the same time
        for i,nums in enumerate(nums):
            print("i :",i)
            print("nums :",nums)
            # if we get a count nums, add the count, else, add -1
            count+=1 if nums else -1
            if count in seen_at:
                ans=max(ans,i-seen_at[count])
            else :
                seen_at[count]=i
        return ans  
    
nums = [0,1]
nums2 = [0,1,0]

sol = Solution()
print(sol.findMaxLength(nums))