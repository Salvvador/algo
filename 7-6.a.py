def fuzzy_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if right > left:
        p, q = partition(arr, left, right)
        fuzzy_sort(arr, left, p - 1)
        fuzzy_sort(arr, q + 1, right)
    return arr


def partition(arr, left, right):
    pivot_val = arr[right]
    j = left
    for i in range(left, right):
        if arr[i][1] < pivot_val[0]:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    k = j
    for i in range(j, right):
        if arr[i][0] < pivot_val[0]:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
    l = k
    for i in range(k, right):
        if arr[i][0] < pivot_val[1]:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
    arr[right], arr[l] = arr[l], arr[right]
    return j, l


arr1 = [(3, 5), (3, 4), (1, 2), (5, 7), (4, 6), (2, 5), (-1, 0)]
arr2 = [(1, 3)]
arr3 = [(6, 7), (0, 1), (10, 11), (2, 3), (8, 9), (4, 5)]
arr4 = [(-1, 2), (4, 7), (1, 3), (2, 4), (3, 6), (3, 5), (1, 3), (5, 7), (1, 2), (3, 7), (0, 2), (-2, 3)]

print(fuzzy_sort(arr1))
print(fuzzy_sort(arr2))
print(fuzzy_sort(arr3))
print(fuzzy_sort(arr4))
