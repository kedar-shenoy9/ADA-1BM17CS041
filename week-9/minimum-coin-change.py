table = []
coin_index = []

def findMinimumNoCoins(d, amount, n):
	#d = denomination set, amount = amount that needs to be made, n = no of denominations
	global table
	global coin_index
	table = [float('inf') for _ in range(amount+1)]
	coin_index = [-1 for _ in range(amount+1)]
	table[0] = 0
	coin_index[0] = 0
	
	#building the table
	for i in range(1, amount+1):
		for j in range(n):
			if d[j] <= i:
				sub_res = table[i-d[j]]
				if sub_res != float('inf') and sub_res+1 < table[i]:
					table[i] = sub_res + 1
					coin_index[i] = j

	return table[amount]

def printTheCoins(amount, d):
	a = amount
	global coin_index
	while a > 0:
		print(d[coin_index[a]], end = " ")
		a = a-d[coin_index[a]]
	print('\n')

if __name__ == "__main__":
	amount = int(input("Enter the amount you want change for "))
	d = list(map(int, input("Enter the denomination array ").split()))
	print("Minimum number of coins :"+str(findMinimumNoCoins(d, amount, len(d))))
	print("The coins used are ")
	printTheCoins(amount, d)
