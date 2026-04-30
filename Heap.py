import heapq

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

# Min heap
heapq.heapify(A)
print("heapified:", A)

heapq.heappush(A, 4)
print("push:", A)

min_val = heapq.heappop(A)
print("pop:", min_val)


# Heap sort (safe)
def heapsort(arr):
    arr = arr.copy()
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


# Max heap
B = [-x for x in A]
heapq.heapify(B)

largest = -heapq.heappop(B)
print("largest:", largest)

# pushpop example
heapq.heappushpop(A, 99)
print("pushpop:", A)


if __name__ == '__main__':
    print("sorted:", heapsort(A))
    #peek
    print('peek', A[0])
    
    #heap from the scratch
    
    C = [-5, 4, 2, 1, 7, 0, 3]
    
    heap = []
    
    for x in C:
        heapq.heappush(heap, x)
        print(heap)