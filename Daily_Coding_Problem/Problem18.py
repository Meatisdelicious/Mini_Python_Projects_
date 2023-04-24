# 6 Invert Binary Tree
 
# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

class Solution:
    def invert_tree(self, root=0, left=None, right=None):
        if not root: 
            return None

        self.invert(root)
        return root
    
    # node = noeud ( ici on cherche à inverser 2 feuilles)
    def invert(self, node):
        if not node:
            return None
        print(self.invert(node.left))
        print(self.invert(node.right))

        node.left, node.right = node.right,node.left
        return node