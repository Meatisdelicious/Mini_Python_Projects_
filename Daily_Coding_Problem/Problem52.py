# w4 6 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.


# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

import numpy as np


class Solution(object):
    def sortedSquares(self, nums):
        array_nums = np.array(nums)
        squared_array = np.square(array_nums)
        sorted_array = np.sort(squared_array)
        return sorted_array


nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]
sol = Solution()
sol.sortedSquares(nums1)
