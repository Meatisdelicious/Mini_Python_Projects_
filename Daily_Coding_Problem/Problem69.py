# w7 75. Sort Colors


# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color
# red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

class Solution(object):
    def sortColors(self, nums):
        sorted_list = []
        while nums:
            sorted_list.append(min(nums))
            nums.remove(min(nums))
        return sorted_list
                    
                     

nums1 = [2,0,2,1,1,0]
nums2 = [2,0,1]
sol = Solution()
print(sol.sortColors(nums2))
