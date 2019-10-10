def knapSack(v, w, weight):
	mat = [[0 for i in range(weight+1)] for j in range(len(v)+1)]
	#starting to fill the matrix
	for i in range(len(v)+1):
		for j in range(weight+1):
			if i == 0 or j == 0:
				mat[i][j] = 0
			elif j-w[i-1] >= 0:
				mat[i][j] = max(mat[i-1][j], v[i-1]+mat[i-1][j-w[i-1]])
			else:
				mat[i][j] = mat[i-1][j]

	print(mat)
	return mat[n][weight]

if __name__ == "__main__":
	n = int(input("Enter the number of items "))
	v = list(map(int, input("Enter the value array ").split()))
	w = list(map(int, input("Enter the weights array ").split()))
	weight = int(input("Enter the capacity of the sack "))
	print(knapSack(v, w, weight))
