# w10 704. Binary Search


# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

class Solution(object):
    def search(self,nums, target):
        count=0
        for n in range(len(nums)):
            if nums[n] != target:
                count+=1
            else :
                return n,print("index :",n)
        if count == len(nums):
            return -1,print("no success")
                
nums = [-1,0,3,5,9,12]
target = 9
nums1 = [-1,0,3,5,9,12]
target1 = 2
sol = Solution()
# sol.search(nums,target)
sol.search(nums1,target1)

class Solution(object):
    def search2(self,nums, target): 
        l,r=0,len(nums)-1
        while l <= r:
            m=(l+r)//2
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else :
                return m
        return -1