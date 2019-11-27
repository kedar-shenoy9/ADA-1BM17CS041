class Node:
    def __init__(self, data, i, j):
        self.data = data
        self.i = i
        self.j = j

def heapify(heap, index):
    low = index
    left = 2*index + 1
    right = 2*index + 2

    if left < len(heap):
        if heap[left].data < heap[low].data:
            low = left
    
    if right < len(heap):
        if heap[right].data < heap[low].data:
            low = right
    
    if low != index:
        temp = heap[low]
        heap[low] = heap[index]
        heap[index] = temp
        heapify(heap, low)

def find_min_range(l, rows, cols):
    my_range = float("inf")
    minimum = float("inf")
    maximum = float("-inf")
    start = -1
    end = -1

    heap = []
    for i in range(rows):
        temp = Node(l[i][0], i, 1)
        heap.append(temp)
        if l[i][0] > maximum:
            maximum = l[i][0]

    #heapify it
    i = (rows//2)-1
    while i>= 0:
        heapify(heap, i)
        i -= 1

    while True:
        minimum = heap[0].data

        if my_range > maximum - minimum + 1:
            my_range = maximum -minimum+1
            start = minimum
            end = maximum

        if heap[0].j < cols:
            heap[0].data = l[heap[0].i][heap[0].j]
            heap[0].j += 1
            if heap[0].data > maximum:
                maximum = heap[0].data
        else:
            break

        i = (rows//2)-1
        while i>=0:
            heapify(heap, i)
            i -= 1

    print(f"The min range is {start} to {end}")

if __name__ == "__main__":
    n = int(input("Enter the number of lists "))
    l = []
    print("Enter the lists")
    for _ in range(n):
        t = list(map(int, input().split()))
        l.append(t)
    
    find_min_range(l, n, len(l[0]))