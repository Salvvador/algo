def hoare_partition(arr, left, right):
    pivot = arr[left]
    i = left - 1
    j = right + 1
    while True:
        j -= 1
        while arr[j] > pivot:
            j -= 1
        i += 1
        while arr[i] < pivot:
            i += 1
        if i < j:
            arr[j], arr[i] = arr[i], arr[j]
        else:
            return j


def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return arr
    p = hoare_partition(arr, left, right)
    quick_sort(arr, left, p)
    quick_sort(arr, p + 1, right)
    return arr


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(quick_sort(arr1))
print(quick_sort(arr2))
print(quick_sort(arr3))