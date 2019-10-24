
def checkMaxHeap(heap):
    n = len(heap)
    for i in range(n//2):
        if 2*i+2 < n:
            comp = max(heap[2*i+1], heap[2*i+2])
        else:
            comp = heap[2*i+1]
        if comp > heap[i]:
            return False

    return True


if __name__ == "__main__":
    heap = list(map(int, input("Enter the heap").split()))
    flag = checkMaxHeap(heap)
    if flag:
        print("It is a max heap")
    else:
        print("It is not a max heap")