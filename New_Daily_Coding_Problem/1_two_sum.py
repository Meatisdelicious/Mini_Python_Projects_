
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = []
        for i in nums: 
            print("i:",i)
            for j in nums:
                print("j :",j)
                if i+j==target:
                    print("[",nums.index(i),",",nums.index(j),"]")
                    list=[nums.index(i),nums.index(j)]
                    return list
nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6


Solution = Solution()

print(Solution.twoSum(nums1,target1))