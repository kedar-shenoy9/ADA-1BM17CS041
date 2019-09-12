def bfs(node, visited, adj_mat, num_nodes):
	queue = []
	visited[node] = True
	queue.append(node)
	while len(queue) > 0:
		temp = queue.pop(0)
		#print the node
		print(temp, end = " ")
		#check for adjacent node which is not visited and put it in the queue
		for i in range(num_nodes):
			if adj_mat[temp][i] == 1 and not visited[i]:
				visited[i] = True
				queue.append(i)

	
	
if __name__ == "__main__":
	num_nodes = int(input("Enter the number of nodes "))

	#visited list to keep track of nodes visited
	visited = [False]*num_nodes

	#adjacency matrix
	adj_mat = []
	for i in range(num_nodes):
		l = list(map(int, input().split()))
		adj_mat.append(l)
	start = int(input("Enter the start node "))
	
	print("\n")
	#call the bfs on the unvisited node
	#for i in range(num_nodes):
		#if not visited[i]:
			#bfs(i, visited, adj_mat, num_nodes)
	bfs(start, visited, adj_mat, num_nodes)

	print("\n")

