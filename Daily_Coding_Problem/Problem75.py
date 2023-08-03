# w9 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total 
# number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        curSum=0
        prefixSum = {0:1}
        for n in nums:
            curSum +=n
            diff =curSum-k
            res+=prefixSum.get(diff,0)
            prefixSum[curSum]=1+prefixSum.get(curSum,0)

        return res 