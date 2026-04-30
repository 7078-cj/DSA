def heapify_down(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_down(arr, n, smallest)


def build_min_heap(arr):
    n = len(arr)
    # start from last non-leaf node
    for i in range(n//2 - 1, -1, -1):
        heapify_down(arr, n, i)
        
if __name__ == "__main__":
    A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

    build_min_heap(A)
    print(A)