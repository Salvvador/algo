def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        current = arr[i]
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = current
    return arr


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(insertion_sort(arr1))
print(insertion_sort(arr2))
print(insertion_sort(arr3))
