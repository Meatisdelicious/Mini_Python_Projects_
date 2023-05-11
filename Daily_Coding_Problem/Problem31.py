# w2 5 169. Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n/2⌋ times.
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        maximum_ele = max(nums, key=nums.count)
        print(maximum_ele)
        count_max_ele_occur = nums.count(maximum_ele)
        if count_max_ele_occur > len(nums)/2:
            return maximum_ele


# O(NlogN)


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        for key in counter:
            if counter[key] > len(nums)//2:
                return key


nums1 = [3, 2, 3, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
sol.majorityElement(nums2)
