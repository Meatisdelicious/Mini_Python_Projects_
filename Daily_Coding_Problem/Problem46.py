# w4 1 101. Symmetric Tree

# Given the root of a binary tree, check whether it
# is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

class Solution(object):
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            (left.val == right.val and dfs(left.left, right.right)
             and dfs(left.right, right.left))
        return dfs(root.left, root.right)


root1 = [1, 2, 2, 3, 4, 4, 3]
root2 = [1, 2, 2, None, 3, None, 3]
sol = Solution()
sol.isSymmetric(root1)
