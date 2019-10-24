class Node:
    def __init__(self, data, i, j):
        self.data = data    #actual data in the node
        self.i = i     #list index
        self.j = j     #position of the next element in the list

def heapify(heap, index):
    low = index
    l = 2*index+1
    r = 2*index+2
    if l < len(heap):
        if heap[l].data < heap[low].data:
            low = l
    
    if r < len(heap):
        if heap[r].data < heap[low].data:
            low = r

    if low != index:
        heap[low] = heap[index]
        heap[index] = heap[low]
        heapify(heap, low)


def findMinRange(l, n):
    myRange = float('inf')
    minimum = float('inf')
    maximum = float('-inf')
    heap = []
    #creating the heap
    for i in range(len(n)):
        t = Node(l[i][0], i, 1)
        heap.append(t)
        if l[i][0] > maximum:
            maximum = l[i][0]

    #heapify the l array
    i = (len(l)//2)-1
    while i>=0:
        heapify(l, i)
        i -= 1

    minimum = heap[0]
    #now we have both minimum and maximum
    while True:
        #check for the range 
        if maximum-miin


if __name__ == "__main__":
    row = int(input("Enter the number of lists "))
    col = int(input("Enter the number of elements in each list "))
    l = []
    print("Enter the lists one per line ")
    for _ in range(row):
        temp = list(map(int, input().split()))
        l.append(temp)
    
    findMinRange(l, row)