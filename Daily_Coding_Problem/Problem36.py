# w3 1 217. Contains Duplicate

# Given an integer array nums, return true if any value
# appears at least twice in the array, and
# return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        duplicates = []
        count = 0
        for i in nums:
            if i in seen:
                duplicates.append(i)
                count += 1
            else:
                seen.add(i)
        print(seen, "---", duplicates, "---", count)

        if count > 0:
            return True, print(True)
        else:
            return False, print(False)


sol = Solution()
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
sol.containsDuplicate(nums1)
sol.containsDuplicate(nums2)
sol.containsDuplicate(nums3)
