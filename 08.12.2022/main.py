import numpy as np

with open('puzzle_input.txt') as filereader:
    data_matrix = np.zeros(shape=(99,99))
    for row, line in enumerate(filereader.readlines()):
        data_matrix[row] = [int(x) for x in line.rstrip()]

visibility_matrix = np.zeros(shape=(99,99))

# Check row visibility
for row_num, row in enumerate(data_matrix):
    # Forwards
    largest_tree = -1
    for col_num, tree in enumerate(row):
        if tree > largest_tree:
            largest_tree = tree
            visibility_matrix[row_num, col_num] = 1

    # backwards
    largest_tree = -1
    for col_num, tree in reversed(list(enumerate(row))):
        if tree > largest_tree:
            largest_tree = tree
            visibility_matrix[row_num, col_num] = 1
    

# Check column visibility
for col_num, col in enumerate(data_matrix.T):
    # Forwards
    largest_tree = -1
    for row_num, tree in enumerate(col):
        if tree > largest_tree:
            largest_tree = tree
            visibility_matrix[row_num, col_num] = 1
    
    # Backwards
    largest_tree = -1
    for row_num, tree in reversed(list(enumerate(col))):
        if tree > largest_tree:
            largest_tree = tree
            visibility_matrix[row_num, col_num] = 1

print(sum(sum(visibility_matrix)))

# Find largest scenic score viewing distance

def calculate_scenic_score(up, down, left, right): 
    return up*down*left*right


left_visibility = np.zeros(shape=(99,99))
right_visibility = np.zeros(shape=(99,99))
up_visibility = np.zeros(shape=(99,99))
down_visibility = np.zeros(shape=(99,99))


def traverse_list_find_visibility(list):
    results = []
    largest_value = -1
    visibility = -1
    previous_value = -1
    for pos, value in enumerate(list):
        if value > largest_value:
            largest_value = value
            visibility = pos
        elif value <= previous_value:
            visibility = 1
        else: 
            visibility = 1
            previous_values = list[:pos]
            for prev_value in reversed(previous_values):
                if prev_value < value:
                    visibility+=1
                else:
                    break

        results.append(visibility)
        previous_value = value
    return results

# Check row visibility
for row_num, row in enumerate(data_matrix):
    # Forwards
    left_visibility[row_num] = traverse_list_find_visibility(row)

    # Backwards
    view_right = traverse_list_find_visibility(list(reversed(row)))
    right_visibility[row_num] = list(reversed(view_right))

# Check column visibility
for col_num, col in enumerate(data_matrix.T):
    # Forwards
    up_visibility[:, col_num] = traverse_list_find_visibility(col)
    # Backwards
    view_down = traverse_list_find_visibility(list(reversed(col)))
    down_visibility[:, col_num] = list(reversed(view_down))
    
total_visibility = left_visibility * right_visibility * up_visibility * down_visibility
print(total_visibility.max())



