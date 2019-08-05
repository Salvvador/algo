import math


def d_arry_get_parent(d, i):
    return math.floor((i - 1) / d)


def d_arry_max_heap_insert(arr, d, key):
    arr.append(key)
    i = len(arr) - 1
    parent = d_arry_get_parent(d, i)
    while parent >= 0 and arr[parent] < arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent
        parent = d_arry_get_parent(d, i)


arr0 = [19, 17, 18, 11, 10, 6, 9, 16, 10, 7, 5, 2]
d_arry_max_heap_insert(arr0, 3, 20)
print(arr0)  # expected: 20, 17, 18, 19, 10, 6, 9, 16, 10, 7, 5, 2, 11