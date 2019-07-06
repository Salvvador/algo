def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(bubble_sort(arr1))
print(bubble_sort(arr2))
print(bubble_sort(arr3))
