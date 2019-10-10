mat = []

def subSequence(word1, word2):
	global mat
	#creating a matrix of size len(word1)*len(word2)
	mat = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
	for i in range(len(word1)+1):
		for j in range(len(word2)+1):
			if i == 0 or j == 0:
				mat[i][j] = 0
			elif word1[i-1] == word2[j-1]:
				mat[i][j] = mat[i-1][j-1] + 1
			else:
				mat[i][j] = max(mat[i-1][j], mat[i][j-1])

	print("Length of the longest common subsequence "+ str(mat[len(word1)][len(word2)]))

def printSub(word1, word2):
	sub = ''
	global mat
	i = len(word1)
	j = len(word2)
	while i>0 and j>0:
		if word1[i-1] == word2[j-1]:
			sub += word1[i-1]
			i -= 1
			j -= 1
		elif mat[i-1][j] > mat[i][j-1]:
			i -= 1
		else:
			j -= 1
	print(sub[::-1])

if __name__ == "__main__":
	word1 = input("Enter the first word ")
	word2 = input("Enter the second word ")
	subSequence(word1, word2)
	printSub(word1, word2)
