


def canPlaced(queen, position, placement):
	for j in range(queen):
		if placement[j] == position or abs(j-queen) == abs(placement[j]-position):
			return False
	return True

def printBoard(placement):
	board = []
	for i in range(len(placement)):
		l = [0]*len(placement)
		board.append(l)
	for i in range(len(placement)):
		board[i][placement[i]] = 1
	for ele in board:
		print(ele, end = "\n")
		#print("\n")

def nQueen(queen, n, placement):
	for i in range(n):
		if(canPlaced(queen, i, placement)):
			placement[queen] = i
			if queen == n-1:
				print("new")
				printBoard(placement)
				
			else:
				nQueen(queen+1, n, placement)

if __name__ == "__main__":
	num_queen = int(input("Enter the number of queens "))
	if num_queen in [1,2,3]:
		print("This doesn't have a solution ")
	else:
		placement = [0]*num_queen
		nQueen(0, num_queen, placement)
	
