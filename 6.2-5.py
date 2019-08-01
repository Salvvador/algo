'''
The code for MAX-HEAPIFY is quite efficient in terms of constant factors, except possibly for the recursive call in
line 10, which might cause some compilers to produce inefficient code. Write an efficient MAX-HEAPIFY that uses an
iterative control construct (a loop) instead of recursion.
'''

import math


def max_heapify_iterative(arr, i):
    while i <= math.ceil(len(arr) / 2):
        left = i * 2 + 1
        right = i * 2 + 2
        highest = i
        if left < len(arr) and arr[highest] < arr[left]:
            highest = left
        if right < len(arr) and arr[highest] < arr[right]:
            highest = right
        if highest == i:
            break
        temp = arr[highest]
        arr[highest] = arr[i]
        arr[i] = temp
        i = highest


arr1 = [4, 8, 1]
arr2 = [1, 8, 4]
arr3 = [8, 1, 4]
arr4 = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

max_heapify_iterative(arr1, 0)
print(arr1)  # expected: 8, 4, 1

max_heapify_iterative(arr2, 0)
print(arr2)  # expected: 8, 1, 4

max_heapify_iterative(arr3, 0)
print(arr3)  # expected: 8, 1, 4

max_heapify_iterative(arr4, 2)
print(arr4)  # expected: 27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0
