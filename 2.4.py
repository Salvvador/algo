import math


def count_no_inversions(arr):
    middle = math.floor(len(arr) / 2)
    l = count_no_inversions_step(arr, 0, middle)
    r = count_no_inversions_step(arr, middle + 1, len(arr) - 1)
    m = merge_and_count_inversions(arr, 0, middle, len(arr) - 1)
    return l + r + m


def count_no_inversions_step(arr, start, end):
    if start >= end:
        return 0
    middle = start + math.floor((end - start) / 2)
    l = count_no_inversions_step(arr, start, middle)
    r = count_no_inversions_step(arr, middle + 1, end)
    m = merge_and_count_inversions(arr, start, middle, end)
    return l + r + m


def merge_and_count_inversions(arr, start, middle, end):
    helper_arr = []
    inversion_count = 0
    l_index = start
    r_index = middle + 1
    while l_index <= middle and r_index <= end:
        if arr[l_index] > arr[r_index]:
            helper_arr.append(arr[r_index])
            inversion_count += (middle - l_index + 1)
            r_index += 1
        else:
            helper_arr.append(arr[l_index])
            l_index += 1
    while l_index <= middle:
        helper_arr.append(arr[l_index])
        l_index = l_index + 1
    while r_index <= end:
        helper_arr.append(arr[r_index])
        r_index = r_index + 1
    i = start
    for x in helper_arr:
        arr[i] = x
        i = i + 1
    return inversion_count


arr1 = [2, 3, 8, 6, 1]
arr2 = [1, 2, 3, 4, 5]
arr3 = [2, 3, 8, 6, 1, 1, 5, 7]
arr4 = [5, 4, 3, 2]
print(count_no_inversions(arr1))
print(count_no_inversions(arr2))
print(count_no_inversions(arr3))
print(count_no_inversions(arr4))
