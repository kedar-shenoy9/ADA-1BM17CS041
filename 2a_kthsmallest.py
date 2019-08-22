def kthsmall(arr, k):
	for i in range(0, k):
		small_pos = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[small_pos]:
				small_pos = j
		temp = arr[small_pos]
		arr[small_pos] = arr[i]
		arr[i] = temp
	return arr[k-1]



l = list(map(int, input("Enter the list of numbers ").split()))
k = int(input("Enter the value of k"))
print(kthsmall(l, k))


'''
output
Enter the list of numbers 43 54 23 56 76
Enter the value of k3
54
'''
