# w10 16. 3Sum Closest

# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = 2**31-1
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j<k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum-target) < abs(closest_sum-target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    j = j+1
                else:
                    k = k-1
        return closest_sum