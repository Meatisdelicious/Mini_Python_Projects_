# Problem #27

# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

open_parenthesis = ["[", "{", "("]
closed_parenthesis = ["]", "}", ")"]


def check(myString):
    # method using stacks
    stack = []
    # iterates through the string
    for i in myString:
        # chooses what type of parenthesis to take (open or closed)
        # 1st case, puts in the stacks only open parenthesis
        if i in open_parenthesis:
            stack.append(i)
        # 2nd case,
        elif i in closed_parenthesis:
            # gets the index of the closed parenthesis (it's position) in the myString
            # Enfin comprisssss !!!!!!!!!
            if len(stack) > 0 and open_parenthesis[closed_parenthesis.index(i)] == stack[-1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Optimised code
def is_nested(myString):
    stack = []
    for i in myString:
        if i in open_parenthesis:
            stack.append(i)
        elif i in closed_parenthesis:
            if stack and open_parenthesis[closed_parenthesis.index(i)] == stack[-1]:
                stack.pop()
            else:
                return False
    return not stack


# to test :
string1 = "{aoizxa[]{()}}"
print(string1, "-", check(string1))
string2 = "[{}{})(]"
print(string2, "-", check(string2))
string3 = "((()"
print(string3, "-", check(string3))
