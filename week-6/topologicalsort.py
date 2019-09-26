
def topologicalSort(adj_mat):
	indegree = [0]*len(adj_mat)
	#initializing the indegree array
	for i in range(len(adj_mat)):
		indegree[i] = 0
		for j in range(len(adj_mat)):
			indegree[i] += adj_mat[j][i]

	#ordering the jobs
	for i in range(len(adj_mat)):
		#find the node with indegree zero
		for j in range(len(indegree)):
			if indegree[j] == 0:
				indegree[j] = -1
				print(j, end = " ")
				for k in range(len(adj_mat)):
					if adj_mat[j][k] == 1:
						indegree[k] -= 1

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
	print("Order of jobs: ")
	topologicalSort(adj_mat)
	print("\n")
	
