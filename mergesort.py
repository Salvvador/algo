import math


def merge_sort(arr):
    middle = math.floor(len(arr) / 2)
    merge_sort_step(arr, 0, middle)
    merge_sort_step(arr, middle + 1, len(arr) - 1)
    merge(arr, 0, middle, len(arr) - 1)
    return arr


def merge_sort_step(arr, start, end):
    if start < end:
        middle = math.floor(start + (end - start) / 2)
        merge_sort_step(arr, 0, middle)
        merge_sort_step(arr, middle + 1, end)
        merge(arr, start, middle, end)


def merge(arr, start, middle, end):
    helper_array = []
    l_index = start
    r_index = middle + 1
    while l_index <= middle and r_index <= end:
        if arr[l_index] > arr[r_index]:
            helper_array.append(arr[r_index])
            r_index = r_index + 1
        else:
            helper_array.append(arr[l_index])
            l_index = l_index + 1
    while l_index <= middle:
        helper_array.append(arr[l_index])
        l_index = l_index + 1
    while r_index <= end:
        helper_array.append(arr[r_index])
        r_index = r_index + 1
    i = start
    for x in helper_array:
        arr[i] = x
        i = i + 1


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(merge_sort(arr1))
print(merge_sort(arr2))
print(merge_sort(arr3))
