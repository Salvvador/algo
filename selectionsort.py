def selection_sort(arr):
    for i in range(0, len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
    return arr


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(selection_sort(arr1))
print(selection_sort(arr2))
print(selection_sort(arr3))
