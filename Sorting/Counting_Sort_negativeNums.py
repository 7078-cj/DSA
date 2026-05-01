A = [5, 3, 2, 1, 3, 3, 7, 2, 2, -2, -5]

def counting_sort(arr):
    n = len(arr)
    
    min_val = min(arr)
    max_val = max(arr)
    
    # Range of values
    range_val = max_val - min_val + 1
    
    counts = [0] * range_val
    
    # Count occurrences (shift by min_val)
    for x in arr:
        counts[x - min_val] += 1
    
    i = 0
    for c in range(range_val):
        while counts[c] > 0:
            arr[i] = c + min_val  # shift back
            i += 1
            counts[c] -= 1

counting_sort(A)
print(A)