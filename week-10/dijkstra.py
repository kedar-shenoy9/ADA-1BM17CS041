def dijkstra(g):
	n = len(g)
	#initialize everythin
	visited = [0]
	dist = [g[0][i] for i in range(n)]
	prev = [0 for i in range(n)]

	count = 0
	#repeat for all nodes
	while count < n-1:
		minimum = 999
		#find the node with minimum cost to reach it
		for i in range(n):
			if dist[i] < minimum and i not in visited:
				minimum = dist[i]
				min_index = i
		
		visited.append(min_index)
		#consider all the edges starting at min_index to the nodes which are not visited
		for i in range(n):
			if dist[min_index]+graph[min_index][i] < dist[i] and i not in visited:
				dist[i] = dist[min_index]+graph[min_index][i]
				prev[i] = min_index

		count += 1

	#print the paths and weights
	for i in range(1, n):
		print("Distance from 0 to "+str(i)+" is "+str(dist[i]))
		print("Path is :")
		end = i
		path = []
		while end != 0:
			
			path.append(end)
			end = prev[end]
		path.append(0)
		print("->".join(map(str, path[::-1])))
		
		



if __name__ == "__main__":
	n = int(input("Enter the number of nodes "))
	graph = []
	for _ in range(n):
		l = list(map(int, input().split()))
		graph.append(l)

	dijkstra(graph)
	
