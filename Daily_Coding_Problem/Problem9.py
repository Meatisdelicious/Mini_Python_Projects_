# Problem #23

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
# Given this matrix, a start coordinate, and an end coordinate, 
# return the minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. 
# You can move up, left, down, and right. 
# You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
#  [t, t, f, t],
#  [f, f, f, f],
#  [f, f, f, f]]

# and start = (3, 0) (bottom left) (3 bcs 0,1,2,3=4) and end = (0, 0) (top left), 
# the minimum number of steps required to reach the end is 7, 
# since we would need to go through (1, 2) because there is a 
# wall everywhere else on the second row. 

matrix = [[0, 0, 0, 0], 
          [1, 1, 1, 1], 
          [0, 0, 0, 1], 
          [0, 0, 0, 0]]
num_rows_matrix = len(matrix)
num_cols_matrix = len(matrix[0])
# Iterate through the matrix in reverse order
# for i in range(start_value,stop_value,step_value)
count=0
for row in range(num_rows_matrix - 1, -1, -1):
    print("---row---", row)
    for element in range(num_cols_matrix - 1, -1, -1):
        matrix_element = matrix[row][element]
        print("ele before filter :",matrix_element)
        row_count=0
        if matrix_element == 0 :
            count+=1
            row_count+=1
            print(row_count)
            skip_row = True
            break
    if skip_row == True:
        print(" ele after ele",matrix_element)
        continue
print("number of steps :",count)