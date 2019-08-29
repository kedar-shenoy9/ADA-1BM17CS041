
def merge(arr, l, m, h):
	n1 = m-l+1
	n2 = h-m
	l1 = []
	l2 = []
	#auxiliary array 1
	for i in range(n1):
		l1.append(arr[l+i])
	
	#auxiliary array 2
	for i in range(n2):
		l2.append(arr[m+1+i])
	
	#merging into arr
	i = 0
	j = 0
	k = l
	while i < n1 and j < n2:
		if l1[i] <= l2[j]:
			arr[k] = l1[i]
			i += 1
		else:
			arr[k] = l2[j]
			j += 1
		k += 1
	
	#adding the remaining elements of l1 and l2 into arr
	while i < n1:
		arr[k] = l1[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = l2[j]
		j += 1
		k += 1	


def mergeSort(arr, l, h):
	if l < h:
		m = (l+(h-1))//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, h)
		merge(arr, l, m, h)


arr = list(map(int, input("Enter the elements of the array ").split()))
mergeSort(arr, 0, len(arr)-1)
print("Array after sorting is ")
for ele in arr:
	print(ele, end = " ")
print("\n")
