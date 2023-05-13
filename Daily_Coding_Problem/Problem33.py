# w2 7 543. Diameter of Binary Tree
# Easy
# 11.3K
# 707
# Companies
# Given the root of a binary tree, 
# return the length of the diameter of the tree.
# The diameter of a binary tree is the length of 
# the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

# The length of a path between two nodes is represented 
# by the number of edges between them.


# ex 1 :
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# ex 2 :
# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        result = [0]

        # depht for search (nested function)
        def dfs(root):
            if not root :
                # height of a null tree
                return -1
            # to find the height of the left subtree
            left =  dfs(root.left)
            right = dfs(root.right) 

            #equasion to find the height of the tree
            result[0] = 2 + left + right
            return 
    


sol = Solution()