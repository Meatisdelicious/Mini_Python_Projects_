class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(node):
    #Si le node est vide, cela stop l'execussion, et il passe à la prochaine node.
    if node is None:
        return
    # Process the current node
    print(node.val)
    # Recursively visit the left subtree
    dfs(node.left)
    # Recursively visit the right subtree
    dfs(node.right)

#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform depth-first search (pre-order traversal)
print("Depth-First Search (Pre-order):")
dfs(root)
