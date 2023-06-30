
# MINE SWEEPER

# Each hash (#) represents a mine and each dash (-) represents a mine-free spot
# Return a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot(number of mines in adjacent cells)

# Functions for iterating
from itertools import product

from copy import deepcopy

#2d lists, 5 columns with rows of 5
original_grid = [ ["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"]]

expected = [["1", "1", "2", "#", "#"],
            ["1", "#", "3", "3", "2"],
            ["2", "4", "#", "2", "0"],
            ["1", "#", "#", "2", "0"],
            ["1", "2", "2", "1", "0"] ]


def mines_adj(grid):
    row = len(grid) #5
    col = len(grid[0]) #5

    if(row == 0):  
        return -1

    # product: equivalent to a nested for-loop
    directions = list(product([0, 1, -1], repeat=2))
    
    # A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
    new_map = deepcopy(grid)    # make a copy of the grid that we edit.
    
#     # loop through the rows  
    for r in range(row):
#         # loop through the columns 
        for c in range(col):
            # if space is mine-free add number 0
            if(grid[r][c] == "-"): 
                count = 0
#                 # next code checks in all directions for a mine
                for dirs in directions:
                    nr = r + dirs[0]
                    nc = c + dirs[1]
                    
                
                    if 0 <= nr < row and  \
                       0 <= nc < col and grid[nr][nc] == "#":
                        count += 1

                new_map[r][c] = str(count)  # writes the count value into the grid location as a string.       
    return new_map

# out is mines_adj function with original grid as input
out = mines_adj(original_grid)
# print(out)
# [['1', '1', '2', '#', '#'], ['1', '#', '3', '3', '2'], ['2', '4', '#', '2', '0'], ['1', '#', '#', '2', '0'], ['1', '2', '2', '1', '0']]

# lines up the grid.
if out == expected:
    print("\nThis is the revealed map")
    for j in range(len(original_grid)):
        print("\n", out[j])
else:
    "There seems to have been a mistake"




