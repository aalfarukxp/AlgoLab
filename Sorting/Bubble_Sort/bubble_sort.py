def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # optimization: stop early if already sorted
            break
    return arr

print(bubble_sort([9, 3, 6, 2, 1, 11]))
print(bubble_sort([12, 16, 14, 1, 2, 3]))
