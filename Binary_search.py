# binary search

A = [-3, -1, 0, 1, 4, 7]

#naive O(n)
if -1 in A:
    print(True)

#traditional BS
#time: O(log n)
#space: O(1)

def binary_search(arr, target):

    N = len(arr)
    L = 0
    R = N - 1

    while L <= R:
        M = L + ((R - L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R  = M - 1
        else:
            L = M + 1
        
    return False

print(binary_search(A, 0))

#Based condition
B = [False, False, False, False, True, True, True, True]

def binary_search_condition(arr):

    N = len(arr)
    L = 0
    R = N - 1
    
    while L < R:
        M = L + ((R - L) // 2)
        
        if B[M]:
            R = M
        else:
            L = M + 1
    return L

print(binary_search_condition(B))
