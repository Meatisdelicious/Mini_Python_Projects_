# problem #197

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.
# Given an array and a number k that's smaller than the length of the array,
# rotate the array to the right k elements in-place.

import numpy as np
test_array = [1, 3, 2, 4, 6]
number_k = 2

# Simple way (using imports)


def rotate_right_by_k(array, k):
    print("original_list :", array)
    rotated_list = np.roll(array, k)
    return print("rotated_list :", rotated_list)


rotate_right_by_k(test_array, number_k)

# hard way (without imports)


def rotate_right_k(array, k):
    # +1 bcs it didn't show the same result as above lol...
    index_after_k = k+1
    rotated_list = []
    for i in array[index_after_k:]:
        rotated_list.append(i)
    index_before_k = abs(k-len(array))
    for j in array[:index_before_k]:
        rotated_list.append(j)
    return print("this is the way : --rotated-hard-list--", rotated_list)


rotate_right_k(test_array, number_k)
