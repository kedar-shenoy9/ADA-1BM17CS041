def floyd(g):
	n = len(g)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				g[i][j] = min(g[i][j], g[i][k]+g[k][j])

	return g


if __name__ == "__main__":
	n = int(input("Enter the number of nodes "))
	graph = []
	for _ in range(n):
		l = list(map(int, input().split()))
		graph.append(l)	
	
	mat = floyd(graph)
	for ele in mat:
		print(ele)
