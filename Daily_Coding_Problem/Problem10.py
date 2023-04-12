# Problem #23

# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. 
# That is, given a stream of numbers, 
# print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2     ---> 2
# 1.5   ---> 2,1 --> 1,2
# 2     ---> 2,1,5 --> 1,2,5
# 3.5   ---> 2,1,5,7 --> 1,2,5,7 --> 2+5/2 = 3.5
# 2     ---> 2,1,5,7,2 --> 1,2,2,5,7 --> = 2
# 2     ---> 2,1,5,7,2,0 --> 0,1,2,2,5,7 --> = 2
# 2     ---> 2,1,5,7,2,0,5 --> 0,1,2,2,5,5,7 --> = 2

number_list = [2, 1, 5, 7, 2, 0, 5]
def median_of_list(random_list):
    temp_list=[]
    for i in random_list:
        temp_list.append(i)
        sorted_temp_list = sorted(temp_list)
        print(sorted_temp_list)

        # if we only have one number
        if len(sorted_temp_list) == 1:
            print("first element of list",sorted_temp_list[0])

        # if we have a list that has a pair lenght
        if len(sorted_temp_list)%2 == 1:
            print("pair list")
        # if we have a list that has an impair lenght
        if len(sorted_temp_list)%2 == 0 :
            print("impair list")
    return 

median_of_list(number_list)