

def dfs(v):
	global visited
	global adj_mat
	global n
	#mark v as visited
	visited[v] = 1
	
	#print v
	print(v, end = "-")
	
	#for every adjacent vertex of v call dfs if not visited
	for i in range(n):
		if adj_mat[v][i] == 1 and visited[i] == 0:
			dfs(i)
	

adj_mat	= []
n = int(input("Enter the number of vertices "))
visited = [0]*n
print("Enter the elements of adjancey matrix (one row in one line)")
for _ in range(n):
	l = list(map(int, input().split()))
	adj_mat.append(l)


#going through each vertex
for i in range(n):
	if visited[i] == 0:
		dfs(i)
		print("\n")

'''
output:

Enter the number of vertices 6
Enter the elements of adjancey matrix (one row in one line)
0 1 1 0 0 1
1 0 0 0 0 0
1 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
1 0 0 0 0 0



0 1 2 5 

3 4 
'''
