# Problem #20

# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node.
# The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

#  !!! Made only with regular lists

first_list = [3, 7, 8, 10]
second_list = [99, 1, 8, 10]

def intersection_list(list1,list2):
    for item_l1 in list1:
        print(item_l1)
        for item_l2 in list2:
            print(item_l2)
            if item_l1 == item_l2:
                print('first element value', item_l1,"and ",item_l2)
                return item_l1
intersection_list(first_list, second_list)









