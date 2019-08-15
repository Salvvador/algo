import math


def partition(arr, left, right):
    pivot = arr[right]
    number_of_pivot_repetitions = 0
    j = left
    for i in range(left, right):
        if arr[i] == pivot:
            number_of_pivot_repetitions += 1
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[right], arr[j] = arr[j], arr[right]
    return j + math.floor(number_of_pivot_repetitions / 2)


arr1 = [3, 43, 12, 12, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4, 5, 5, 5, 5, 5, 5]
arr3 = [5, 4, 3, 2, 1]

print(partition(arr1, 0, len(arr1) - 1))  # expected: 7
print(partition(arr2, 0, len(arr2) - 1))  # expected: 3
print(partition(arr3, 0, len(arr3) - 1))  # expected: 0
