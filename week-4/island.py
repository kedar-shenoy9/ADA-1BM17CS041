#global variables
rowNbr = [-1,-1,-1,0,0,1,1,1]
colNbr = [-1,0,1,-1,1,-1,0,1]


def isSafe(adj_mat, row, col, visited_mat, n):
	return row>=0 and row<=n and col>=0 and col<=n and adj_mat[row][col] and not visited_mat[row][col]

def dfs(adj_mat, i, j, visited_mat, n):
	global rowNbr
	global colNbr
	visited_mat[i][j] = True
	for k in range(8):
		if isSafe(adj_mat, i+rowNbr[k], j+colNbr[k], visited_mat, n):
			dfs(adj_mat, i+rowNbr[k], j+colNbr[k], visited_mat, n)


if __name__ == "__main__":
	adj_mat	= []
	visited_mat = []
	island_count = 0
	n = int(input("Enter the number of vertices "))

	#initializing the visited matrix
	for _ in range(n):
		l = [False]*n
		visited_mat.append(l)


	#taking the elements of the adjanc matrix
	print("Enter the elements of adjancey matrix (one row in one line)")
	for _ in range(n):
		l = list(map(int, input().split()))
		adj_mat.append(l)

	#driver code
	for i in range(n):
		for j in range(n):
			if adj_mat[i][j] == 1 and visited_mat[i][j] == False:
				dfs(adj_mat, i, j, visited_mat, n)
				island_count += 1
	print(island_count)			

'''
output:

Enter the number of vertices 5
Enter the elements of adjancey matrix (one row in one line)
1 0 0 1 0
0 0 1 0 0
0 1 1 1 0
0 1 0 1 0
0 0 0 0 0
2
'''
