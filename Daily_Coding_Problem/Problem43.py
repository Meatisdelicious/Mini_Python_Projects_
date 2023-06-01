# w3 10 136. Single Number

# Given a non-empty array of integers nums,
# every element appears twice except for one.
# Find that single one.

# You must implement a solution with a linear
# runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1


class Solution(object):
    def singleNumber(self, nums):
        news_list = []
        for i in range(len(nums)):
            print("i", nums[i])
            for j in range(0, len(nums)):
                if j == i:
                    
                print("j", nums[j])

        return


nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]
sol = Solution()
print(sol.singleNumber(nums1))
