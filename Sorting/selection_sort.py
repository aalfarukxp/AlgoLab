def selection_sort(arr):
    n = len(arr) #length of the element
    for i in range(n -1 ): # # go through each index except the last
        min_index = i
        for j in range (i + 1, n): #check rest of the list
            if arr[j] < arr [min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] #swap
    return arr

print(selection_sort([9, 3, 6, 2, 1, 11]))
print(selection_sort([12, 16, 14, 1, 2, 3]))