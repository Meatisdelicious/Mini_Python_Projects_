# problem #221

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Zillow.

# Let's define a "sevenish" number to be one which is either a power of 7,
# or the sum of unique powers of 7.
# The first few sevenish numbers are 1, 7, 8, 49, and so on.
# Create an algorithm to find the nth sevenish number.

# Working solution
def get_nth_sevenish_num(number: int) -> int:
    curr = 1
    curr_iteration = 1
    while curr < number:
        curr_iteration += 1
        curr += curr_iteration

    curr -= curr_iteration
    result = 7 ** (curr_iteration - 1)
    curr_to_add = 1

    for _ in range(number - curr - 1):
        result += curr_to_add
        curr_to_add *= 7
    return result


if __name__ == "__main__":
    print(get_nth_sevenish_num(1))  # 1 = 7 ^ 0
    print(get_nth_sevenish_num(2))  # 7 = 7 ^ 1
    print(get_nth_sevenish_num(3))  # 8 = 7 ^ 0 + 7 ^ 1
    print(get_nth_sevenish_num(4))  # 49 = 7 ^ 2
    print(get_nth_sevenish_num(5))  # 50 = 7 ^ 0 + 7 ^ 2
    print(get_nth_sevenish_num(6))  # 57 = 7 ^ 0 + 7 ^ 1 + 7 ^ 2

    
#  This doesn't work for shit...
import math
numb = 49
def sevenish_number(number):

    if math.sqrt(number) % number :
        print("is a power of 7 :",math.sqrt(number))

    for i in range(0,number,1):
        temp1=number*i
        
        for j in range(i,number,1):
            temp2=number*j + temp1
            if temp2 == math.sqrt(7):
                print("is a sum of unique powers of", temp2)
    else : 
        print("this number is not a power of 7 :", number)
    return 

sevenish_number(numb)