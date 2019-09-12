from math import sqrt

#function to check if that number is in that column
def inCol(grid, col, num, n):
	for i in range(n):
		if grid[i][col] == num:
			return True
	return False

#function to check if that number is in that row
def inRow(grid, row, num, n):
	for i in range(n):
		if grid[row][i] == num:
			return True
	return False

#function to check if that number is in that box
def inBox(grid, row, col, num, n):
	box_size = int(sqrt(n))
	for i in range(box_size):
		for j in range(box_size):
			if grid[i+row][j+col] == num:
				return True
	return False

#function to check if it's safe to insert num in grid[row][col]
def isSafe(grid, row, col, num, n):
	return not inRow(grid, row, num, n) and not inCol(grid, col, num, n) and not inBox(grid, row-row%int(sqrt(n)), col-col%int(sqrt(n)), num, n)



def findUnallocated(grid, n, l):
	#find an unallocated position	
	for i in range(n):
		for j in range(n):
			if grid[i][j] == 0:
				l[0] = i
				l[1] = j
				return True
	return False

def solveSudoku(grid, n):
	#find an unallocated spot
	l = [0,0] #for storing the row and column number 
	
	if not findUnallocated(grid, n, l):
		return True
	
	#row and column will be passed in l by reference
	row = l[0]
	col = l[1]
	
	#assign a number to the unallocated spot and check if it is solved
	for i in range(1, n+1):
		#check if it is safe to assign that number
		if isSafe(grid, row, col, i, n):
			grid[row][col] = i
			if solveSudoku(grid, n):
				return True
			#else make grid[row][col] = 0
			grid[row][col] = 0
	
	return False

def printGrid(grid, n):
	for i in range(n):
		for j in range(n):
			print(grid[i][j], end = " ")
		print("\n")

if __name__ == "__main__":
	grid = []

	#taking the input from the user
	n = int(input("Enter the size of the grid "))
	print("Enter one row per line ")
	for i in range(n):
		l = list(map(int, input().split()))
		grid.append(l)
	
	#trying to solve the sudoku
	if solveSudoku(grid, n):
		print("\n")
		printGrid(grid,n)
	else:
		print("No solution")
