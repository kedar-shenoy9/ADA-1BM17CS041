def bin_search(a, ele):
	beg = 0
	end = len(a)-1
	while beg<=end:
		mid = (beg+end)//2
		if ele == a[mid]:
			return 1
		elif ele<a[mid]:
			end = mid-1
		else:
			beg = mid+1
	return -1

f = open("bin.txt")
l = f.readlines()
t = int(l[0])
t = t*2
l.pop(0)
l1 = []
for item in l:
	l1.append(list(map(int, item.split())))
while True:
	if len(l1)==0:
		break
	else:
		print(bin_search(l1[1], l1[0][1]))
		l1.pop(0)
		l1.pop(0)
