"""
Problem:
find the number of paths you can take through a grid
you can only go right and down (which also means you can only enter along the left and top sides)


Solution:
Buttom Up Dynamic Programming
Basic idea is that the number of ways to get to a grid cell is the sum of:
  1. all the ways to get to the cell on the right
  2. plus all the ways to get to the cell above you
(but the entry points/boundaries must be initialized as 1)

time complexity: avg/worst case are all the same - O(n^2) (must visit all the rows and columms once)
space complexity: avg/worst case are all the same - O(n^2) (create a dp table of n*n size)

this same approach can be extended to problems like:
- adding values to each of the cells to create sort of a topography
- find the fastest way through a grid (use min values from predeeding cels + 1 at each cell)
- coin change problem 1 - smallest number of coins to get to a value
- coin change problem 2 - number of ways to use coins to get to a value
"""

def num_paths(n):
	# find the total number of possible paths in an n x n grid
	num_grid_points = n + 1
	grid = [[0 for i in range(num_grid_points)] for j in range(num_grid_points)]
	#initialize boundary conditions
	for col in range(len(grid)):
		grid[col][0] = 1
		grid[col][len(grid) - 1] = 1
	for row in range(len(grid)):
		grid[0][row] = 1
		grid[len(grid) - 1][row] = 1
	# calc num paths using dynamic programming concepts
	for row in range(1, len(grid)):
		for col in range(1, len(grid)):
			grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
	for row in grid:
		for col in row:
			print(col, end = " ")
		print()
	return grid[-1][-1]

print(num_paths(10))