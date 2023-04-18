# 2 Valid parenthesis 

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# ,determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

s = "()"
s2= "()[]{}"
s3= "(]"

def valid_parenthsis(string_s):
    open_parenthesis = ["[", "{", "("]
    closed_parenthesis = ["]", "}", ")"]
    stack=[]
    for element in string_s:
        if element in open_parenthesis :
            # to store it in a bibliothèque
            stack.append(element)
            
        elif element in closed_parenthesis:
            # Stack[-1]  ---> meaning, the element that last entered the stack (fist in, first out)
            # Si l'index de la parenthèse fermée est egale au dernier element pris du stack, alors on peut le retirer
            # Ainsi, si on retourne rien, on a bien des parenthèses pair, dc c'est balenced.
            if len(stack) > 0 and open_parenthesis[closed_parenthesis.index(element)] == stack[-1]:
                stack.pop()

    if len(stack)==0:
        return "balanced"
    else :
        return "unbalanced"

print(valid_parenthsis(s))
print(valid_parenthsis(s2))
print(valid_parenthsis(s3))