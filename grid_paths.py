# Buttom Up Dynamic Programming approach to number of paths through a grid

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