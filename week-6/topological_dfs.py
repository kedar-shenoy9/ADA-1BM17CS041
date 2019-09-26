
def topologicalSort(vertex):
	global adj_mat
	global visited
	global stack
	visited[vertex] = 1
	for i in range(len(adj_mat)):
		if adj_mat[vertex][i] == 1 and visited[i] == 0:
			topologicalSort(i)
	stack.append(vertex)

if __name__ == "__main__":
	jobs = []
	adj_mat = []
	n = int(input("Enter the number of job pairs "))
	print("Enter the job pairs one per line ")
	for i in range(n):
		l = list(map(int, input().split()))
		jobs.append(l)
	for i in range(n):
		l = [0]*n
		adj_mat.append(l)
	for pair in jobs:
		adj_mat[pair[1]][pair[0]] = 1
	visited = [0]*len(adj_mat)
	breakValue = False
	stack = []
	
	for i in range(len(adj_mat)):
		for j in range(len(adj_mat)):
			if adj_mat[i][j] == 1:
				topologicalSort(i)
				breakValue = True
				break
		if breakValue:
			break
	print("Order of jobs :")
	while len(stack) > 0:
		print(stack.pop(), end = " ")
	print("\n")
