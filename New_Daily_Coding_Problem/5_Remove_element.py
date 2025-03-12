class Solution(object):
    def wasa(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        seen=set()
        seen.add(val)
        print("seen :",seen)
        for i in range(len(nums) - 1, -1, -1):
            print("i",i)
            if nums[i] in seen:
                print("nums[i]",nums[i])
                nums.pop(i)
                continue
        return len(nums)

sol=Solution()
nums = [3,2,2,3]
val=3
nums1 = [0,1,2,2,3,0,4,2]
val1=3

print(sol.wasa(nums,val))
# print(sol.wasa(nums1,val1))