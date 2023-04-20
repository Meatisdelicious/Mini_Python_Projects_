# 5 Valid palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase
#  letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
import re
def Valid_palindrome(string):
    temp_string = re.sub(r'[^a-zA-Z0-9]', '', string)
    pre_processed_string=temp_string.lower()
    string_to_list =[]
    for i in pre_processed_string:
        string_to_list.append(i)

    string_to_list_reverse=string_to_list[::-1]
    if string_to_list == string_to_list_reverse :
        return True
    else :
        return False 

s = "A man, a plan, a canal: Panama"
s2= "race a car"
s3= " "
print(Valid_palindrome(s))
print(Valid_palindrome(s2))
print(Valid_palindrome(s3))