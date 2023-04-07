# Problem #23

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
# Given this matrix, a start coordinate, and an end coordinate, 
# return the minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. 
# You can move up, down, right, left. 
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

from collections import deque
def is_valid_move(matrix, row, col):
    """
    Helper function to check if a given move is valid
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
        return False
    # Check if the element at the given row and col is equal to 0
    if matrix[row][col] != 0:
        return False
    return True

def min_steps_to_reach_end(matrix, start, end):
    """
    Function to find the minimum number of steps to reach from start to end coordinate on the given board
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    queue = deque([(start[0], start[1], 0)])  # Using a deque for BFS
    visited = set([(start[0], start[1])])  # Keep track of visited coordinates
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move

    while queue:
        row, col, steps = queue.popleft()
        if (row, col) == end:
            return steps  # Return the steps once end coordinate is reached

        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if is_valid_move(matrix, new_row, new_col) and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))
    return None  # If no path is found

def check_possible_path(function):
    if function is not None :
        print(f"The minimum number of steps to reach the end is {function}.")
    else:
        print("There is no possible path to reach the end.")    

# Example usage:
matrix = [[0, 0, 0, 0], 
          [1, 1, 0, 1], 
          [0, 0, 0, 0], 
          [0, 0, 0, 0]]
start = (3, 0)
end = (0, 0)
check_possible_path(min_steps_to_reach_end(matrix, start, end))




#  First clue... not finished

# Iterate through the matrix in reverse order
# for i in range(start_value,stop_value,step_value)
def path_in_matrix(matrix):
    num_rows_matrix = len(matrix)
    num_cols_matrix = len(matrix[0])
    total_count=0
    for row in range(num_rows_matrix - 1, -1, -1):
        print("---------row-----------", row)
        row_count=0
        for element in range(num_cols_matrix - 1, -1, -1):
            matrix_element = matrix[row][element]
            print("ele before filter :",matrix_element)
            total_count+=1
            row_count+=1
            if matrix_element == 0 :
                skip_row = True
                break
            matrix_count_1=0
            if matrix_element==1 :
                matrix_count_1+=1
                if matrix_count_1 == 3:
                    print("NUll")
        print("--row_st_ct-- :",row_count)
        if skip_row == True:
            print("   ele after filt",matrix_element)
            continue
        else :
            print("Null", False), False
    print("\n Total_number_of_steps :",total_count)