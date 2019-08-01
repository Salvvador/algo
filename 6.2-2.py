'''
Starting with the procedure MAX-HEAPIFY, write pseudocode for the procedure MIN-HEAPIFY(A,i), which performs the
corresponding manipulation on a minheap. How does the running time of MIN-HEAPIFY compare to that of MAXHEAPIFY?
'''


def min_heapify(arr, i):
    left = i * 2 + 1
    right = i * 2 + 2
    smallest = i
    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        return min_heapify(arr, smallest)


arr1 = [4, 8, 1]
arr2 = [1, 8, 4]
arr3 = [4, 1, 8]
arr4 = [1, 8, 4, 10, 12, 3, 5]

min_heapify(arr1, 0)
print(arr1)  # expected: 1, 8, 4

min_heapify(arr2, 0)
print(arr2)  # expected: 1, 8, 4

min_heapify(arr3, 0)
print(arr3)  # expected: 1, 4, 8

min_heapify(arr4, 2)
print(arr4)  # expected: 1, 8, 3, 10, 12, 4, 5
