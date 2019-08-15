def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return arr
    p = partition(arr, left, right)
    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[right]
    j = left
    for i in range(left, right):
        if arr[i] >= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[right], arr[j] = arr[j], arr[right]
    return j


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(quick_sort(arr1))
print(quick_sort(arr2))
print(quick_sort(arr3))
