# read in grid of ints from in/day8.txt 
import math


in_file = open('in/day8.txt')
st = in_file.read()
in_file.close()

grid = [[int(x) for x in y] for y in st.splitlines()]
visible = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
# from the left
for i, line in enumerate(grid):
    line_min = -1
    for j, tree in enumerate(line):
        if tree > line_min:
            visible[i][j] = True
            line_min = tree
# from the right
for i, line in enumerate(grid):
    line_min = -1
    for j in range(len(line)-1, -1, -1):
        if line[j] > line_min:
            visible[i][j] = True
            line_min = line[j]
# from the top
for j, col in enumerate(zip(*grid)):
    col_min = -1
    for i, tree in enumerate(col):
        if tree > col_min:
            visible[i][j] = True
            col_min = tree
# from the bottom
for j, col in enumerate(zip(*grid)):
    col_min = -1
    for i in range(len(col)-1, -1, -1):
        if col[i] > col_min:
            visible[i][j] = True
            col_min = col[i]
# count visible trees
print("Part 1: ")
print(sum([sum([1 for x in y if x]) for y in visible]))

# Part 2
max_vis_score = 0
for i, line in enumerate(grid):
    for j, tree in enumerate(line):
        # right
        for k in range(j+1, len(line)):
            if line[k] >= tree:
                break
        visible_trees = k - j
        # left
        for k in range(j-1, -1, -1):
            if line[k] >= tree:
                break
        visible_trees *= j - k
        # top
        for k in range(i-1, -1, -1):
            if grid[k][j] >= tree:
                break
        visible_trees *= i - k
        # bottom
        for k in range(i+1, len(grid)):
            if grid[k][j] >= tree:
                break
        visible_trees *= k - i
        if visible_trees > max_vis_score:
            max_vis_score = visible_trees
print(max_vis_score)