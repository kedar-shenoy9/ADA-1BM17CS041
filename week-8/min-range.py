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
        temp = heap[low]
        heap[low] = heap[index]
        heap[index] = temp
        heapify(heap, low)

def findMinRange(l, n):
    my_range = float("inf")
    minimum = float("inf")
    maximum = float("-inf")
    start = -1
    end = -1

    #create a heap with first elements of all the lists
    heap = []
    for i in range(n):
        temp = Node(l[i][0], i, 1)
        heap.append(temp)
        if l[i][0] > maximum:
            maximum = l[i][0]

    #heapify it
    i = (n//2)-1
    while i>=0:
        heapify(heap, i)
        i -= 1

    #continue until you reach the last element in any list
    while True:
        print('blah')
        minimum = heap[0].data
        if maximum-minimum+1 < my_range:
            my_range = maximum-minimum+1
            start = minimum
            end = maximum

        #replace the root of the heap with the next element of the same list
        if heap[0].j < len(l[0]):
            heap[0].data = l[heap[0].i][heap[0].j]
            heap[0].j += 1
            if heap[0].data > maximum:
                maximum = heap[0].data

        else:
            break
    
        #heapify again
        i = (n//2)-1
        while i>=0:
            heapify(heap, i)
            i -= 1

    print(f"The range is {minimum} to {maximum}")



if __name__ == "__main__":
    row = int(input("Enter the number of lists "))
    col = int(input("Enter the number of elements in each list "))
    l = []
    print("Enter the lists one per line ")
    for _ in range(row):
        temp = list(map(int, input().split()))
        l.append(temp)
    
    findMinRange(l, row)
