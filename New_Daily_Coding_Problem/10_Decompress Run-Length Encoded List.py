class Solution(object):
    def wasa(self, nums):
        result_list=[]
        for i in range(0,len(nums),2):
            freq=nums[i]
            val=nums[i+1]
            print("freq :",freq)
            print("      val:",val)
            for i in range(freq):
                result_list.append(val)
        return result_list

nums1 = [1,2,3,4]
nums2 = [1,1,2,3]
sol=Solution()
print(sol.wasa(nums1))
print(sol.wasa(nums2))