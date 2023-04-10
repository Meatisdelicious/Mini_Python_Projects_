# A unival tree (which stands for "universal value")
# is a tree where all
# nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

# notes random : https://www.karkidi.com/Find-Jobs
# https://pythontutor.com/visualize.html#mode=display
# Explanation video
# https://www.youtube.com/watch?v=7HgsS8bRvjo

# Creating node class
class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# Creating root node
def countSubTree(root,count):
    if root is None:
        return True
    left = countSubTree(root.left,count)
    right = countSubTree(root.right,count)

    # En gros, danc ces "if", on regarde les différents cas ou l'on peut obtenir des "univals".
    # Check les branches mère (root) et filles(left/right)
    # S'il n'y a pas de valeur ni à droite, ni à gauche, --> pas d'unival --> false
    if left == False or right == False:
        return False
    # Si le root fille gauche à une valeur différente du root mère
    if root.left and root.val != root.right.val:
        return False
    # Si le root fille droite à une valeur différente du root mère
    if root.right and root.val != root.right.val:
        return False
    # if all the above cases are not true,
    # ie : if the root value matches with the children
    # When this case is reached, we increment the count
    count[0]+=1
    return True

# counts the number of subtrees
def countTrees(root):
    count=[0]
    # calls the previous function and counts the ones that returned true (the unival one only)
    countSubTree(root,count)
    return count[0]


tree = Node(0,Node(1),Node(0,Node(1,Node(1),Node(1)),Node(0)))
print("No. Of universal subtrees=",countTrees(tree))

