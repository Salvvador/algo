def partition_with_repetitions(arr, left, right):
    pivot = arr[right]
    j = left
    number_of_eq_values = 0
    for i in range(left, right):
        if arr[i] == pivot:
            number_of_eq_values += 1
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[right], arr[j] = arr[j], arr[right]
    return j, j + number_of_eq_values


arr1 = [3, 43, 12, 12, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4, 5, 5, 5, 5, 5, 5]
arr3 = [5, 4, 3, 2, 1]

print(partition_with_repetitions(arr1, 0, len(arr1) - 1))  # expected: 6, 8
print(partition_with_repetitions(arr2, 0, len(arr2) - 1))  # expected: 1, 6
print(partition_with_repetitions(arr3, 0, len(arr3) - 1))  # expected: 0, 0
