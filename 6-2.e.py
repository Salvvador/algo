import math


def d_arry_get_parent(d, i):
    return math.floor((i - 1) / d)


def d_arry_heap_increase_key(arr, d, i, key):
    if arr[i] > key:
        return
    arr[i] = key
    parent = d_arry_get_parent(d, i)
    while parent >= 0 and arr[parent] < arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent
        parent = d_arry_get_parent(d, i)


arr0 = [19, 17, 18, 11, 10, 6, 9, 16, 10, 7, 5, 2]
d_arry_heap_increase_key(arr0, 3, 3, 20)
print(arr0)  # expected: 20, 17, 18, 19, 10, 6, 9, 16, 10, 7, 5, 2