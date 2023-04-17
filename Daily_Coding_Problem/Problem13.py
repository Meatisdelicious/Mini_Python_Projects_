# Two sums 

# Link to study plan easy problems : 
# https://www.techinterviewhandbook.org/grind75

# Given an array of integers "nums" and an integer "target", 
# return indices of the two numbers such that they add up to "target".
# You may assume that each input would have exactly one solution,  (simplifies shit a loooot)
# and you may not use the same element twice.

# You can return the answer in any order.

# Example :

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

# ex1
nums1 = [2,7,11,15]
target1 = 9
# ex2
nums2 = [3,2,4]
target2 = 6
# ex3
nums3 = [3,3], 
target3 = 6

def Two_sums(array, target):

    list_restult = []
    for i in array :
        print("i--",i)
        # index = array.index(i)
        # print("index :",index)
        for j in array:
            if j + i == target:
                index_I = array.index(i)
                index_J = array.index(j)
                list_restult=[index_I,index_J]
                list_restult.sort()
                print("index_I",index_J,"index_J",index_I)

            
            print("j----",j)
    return print("----final anwser----",list_restult)

Two_sums(nums1,target1)
Two_sums(nums2,target2)
# Two_sums(nums3,target3)