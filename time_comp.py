import random
import time

def bub_sort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	return arr


def sel_sort(arr):
	for i in range(len(arr)-1):
		small_pos = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[small_pos]:
				small_pos = j
		temp = arr[small_pos]
		arr[small_pos] = arr[i]
		arr[i] = temp
	return arr


arr = []
n = 50000
for i in range(n):
	arr.append(random.randint(0, 100))
arr1 = arr

#for bubble sort
start1 = time.time()
l1 = bub_sort(arr)
stop1 = time.time()

#for selection sort
start2 = time.time()
l2 = sel_sort(arr1)
stop2 = time.time()

#difference
bub = stop1-start1
sel = stop2-start2

with open("graph_data.txt", "a") as f:
	f.write(str(n)+" "+str(bub)+" "+str(sel)+"\n")


