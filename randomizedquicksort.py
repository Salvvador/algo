import random


def randomized_quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if right > left:
        p = randomized_partition(arr, left, right)
        randomized_quick_sort(arr, left, p - 1)
        randomized_quick_sort(arr, p + 1, right)
    return arr


def randomized_partition(arr, left, right):
    i = random.randint(left, right)
    arr[right], arr[i] = arr[i], arr[right]
    return partition(arr, left, right)


def partition(arr, left, right):
    pivot = arr[right]
    j = left
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    arr[j], arr[right] = arr[right], arr[j]
    return j


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(randomized_quick_sort(arr1))
print(randomized_quick_sort(arr2))
print(randomized_quick_sort(arr3))
