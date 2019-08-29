
def partition(arr, l, h):
	pivot_pos = l
	i = l+1
	for j in range(l+1, h+1):
		if arr[j] < arr[pivot_pos]:
			arr[j], arr[i] = arr[i], arr[j]
			i += 1
	arr[pivot_pos], arr[i-1] = arr[i-1], arr[pivot_pos]
	return i-1


def quickSort(arr, l, h):
	if l < h:
		p = partition(arr, l, h)
		quickSort(arr, l, p-1)
		quickSort(arr, p+1, h)


arr = list(map(int, input("Enter the list of the number ").split()))
quickSort(arr, 0, len(arr)-1)
print("After sorting the array is ")
for ele in arr:
	print(ele, end = " ")
print("\n")
