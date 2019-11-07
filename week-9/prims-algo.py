def prims(graph, n):
	w = 0
	#adding the node 0 to the vertex set of minimal spanning tree
	vertex_set = [0]
	edges_set = []
	
	for i in range(1, n):
		minimum = float('inf')
		index = float('inf')
		for j in vertex_set:
			for k in range(n):
				#if node k is in vertex_set skip it
				if k in vertex_set:
					continue
				else:
					if graph[j][k] < minimum:
						minimum = graph[j][k]
						index = k
						edge = (j,k)

		#add index to the vertex_set
		vertex_set.append(index)
		edges_set.append(edge)
		w += minimum
	
	print(edges_set)
	return w

if __name__ == "__main__":
	graph = []
	n = int(input("Enter the number of nodes "))
	print("Enter the weight matrix of the graph one row per line, if there is no edge enter weight as 999")
	#take the weight matrix from the user
	for _ in range(n):
		l = list(map(int, input().split()))
		graph.append(l)

	#get the weight of the minimal spanning tree
	weight = prims(graph, n)
	print("Weight of the minimum spanning tree "+str(weight))
