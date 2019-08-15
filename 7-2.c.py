import random


def partition_with_repetitions(arr, left, right):
    pivot = arr[right]
    j = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    k = j
    for i in range(j, right):
        if arr[i] == pivot:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
    arr[right], arr[k] = arr[k], arr[right]
    return j, k


def randomized_partition_with_repetitions(arr, left, right):
    i = random.randint(left, right)
    arr[i], arr[right] = arr[right], arr[i]
    return partition_with_repetitions(arr, left, right)


def randomized_quick_sort_with_repetitions(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        p, q = randomized_partition_with_repetitions(arr, left, right)
        randomized_quick_sort_with_repetitions(arr, left, p - 1)
        randomized_quick_sort_with_repetitions(arr, q + 1, right)
    return arr



arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]
arr4 = [10, 5, 5, 5, 4, 4, 3, 2, 77, 1, 5, 5, 5, 3]

print(randomized_quick_sort_with_repetitions(arr1))
print(randomized_quick_sort_with_repetitions(arr2))
print(randomized_quick_sort_with_repetitions(arr3))
print(randomized_quick_sort_with_repetitions(arr4))
