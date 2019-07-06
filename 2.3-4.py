'''
Insertion sort can be expressed as a recursive procedure as follows. In order to sort A[1..n], we recursively sort
A[1..n−1] and then insert A[n] into the sorted array A[1..n−1]. Write a recurrence for the running time of this
recursive version of insertion sort.
'''


def insertion_sort_recursive(arr):
    insertion_sort_recursive_step(arr, len(arr) - 1)
    return arr


def insertion_sort_recursive_step(arr, n):
    if n == 0:
        return
    insertion_sort_recursive_step(arr, n - 1)
    current = arr[n]
    i = n - 1
    while i >= 0 and arr[i] > current:
        arr[i + 1] = arr[i]
        i = i - 1
    arr[i + 1] = current


arr1 = [3, 12, 43, 1, 32, 11, 11, 3, 4, 12]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(insertion_sort_recursive(arr1))
print(insertion_sort_recursive(arr2))
print(insertion_sort_recursive(arr3))
