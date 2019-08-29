import random
import time

def bub_sort(arr):
	bub_count = 0 #number of comparisons
	#algorithm part
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			bub_count += 1
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	return bub_count


def sel_sort(arr):
	sel_count = 0 #number of comparisons
	#algorithm part
	for i in range(len(arr)-1):
		small_pos = i
		for j in range(i+1, len(arr)):
			sel_count += 1
			if arr[j] < arr[small_pos]:
				small_pos = j
		temp = arr[small_pos]
		arr[small_pos] = arr[i]
		arr[i] = temp
	return sel_count

#merge sort
mer_count = 0
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
		global mer_count
		mer_count += 1
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

n = 100
print(f"Initialising the array of size {n} with random numbers ")
arr = []
for _ in range(n):
	arr.append(random.randint(0, 100))

arr1 = arr
arr2 = arr
mergeSort(arr2, 0, len(arr2)-1)

print("Number of comparisons in bubble sort "+str(bub_sort(arr)))
print("Number of comparisons in selection sort "+str(sel_sort(arr1)))
print("Number of comparisons in merge sort "+str(mer_count))

