# w7 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

class Solution(object):
    def rotate(self, nums, k):
        elements_before_k = nums[:k]
        print("elements_before_k",elements_before_k)
        elements_after_k = nums[k:]
        print("elements_after_k",elements_after_k)
        result = elements_after_k+elements_before_k
        return result,print(result)
nums = [1,2,3,4,5,6,7]
k = 3
nums1 = [-1,-100,3,99]
k1 = 2
sol = Solution()
sol.rotate(nums,k)
sol.rotate(nums1,k1)