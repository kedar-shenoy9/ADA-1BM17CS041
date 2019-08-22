def klarge(arr, k):
	for i in range(0, k):
		big_pos = i
		for j in range(i+1, len(arr)):
			if arr[j] > arr[big_pos]:
				big_pos = j
		temp = arr[big_pos]
		arr[big_pos] = arr[i]
		arr[i] = temp
	return arr[0:k]



l = list(map(int, input("Enter the list of numbers ").split()))
k = int(input("Enter the value of k"))
newL = klarge(l, k)
print(newL)


'''
output
Enter the list of numbers 65 45 67 2 54     
Enter the value of k3
[67, 65, 54]
'''
