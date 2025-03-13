class Solution(object):
    def wasa(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1=set(nums1)
        print("set1",set1)
        set2=set(nums2)
        print("set2",set2)
        test=set1&set2
        print("test   :",test)
        result = list(set1&set2)
        return result
nums1 = [1,2,2,1]
nums2 = [2,2]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
sol=Solution()
print(sol.wasa(nums1,nums2))
print(sol.wasa(nums3,nums4))
