def heap_delete(arr, i):
    arr[i], arr[len(arr) - 1] = arr[len(arr) - 1], arr[i]
    heapify(arr, i)
    arr.pop()


def heapify(arr, i):
    left = i * 2 + 1
    right = i * 2 + 2
    smallest = i
    if left < len(arr) and arr[left] > arr[smallest]:
        smallest = left
    if right < len(arr) and arr[right] > arr[smallest]:
        smallest = right
    if smallest != i:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        return heapify(arr, smallest)


heap = [12, 7, 9, 3, 6, 8, 2, 1, 0, -3]

current = heap.copy()
heap_delete(current, 0)
print(current)  # expected: 9, 7, 8, 3, 6, -3, 2, 1, 0

current = heap.copy()
heap_delete(current, 2)
print(current)  # expected: 12, 7, 8, 3, 6, -3, 2, 1, 0

current = heap.copy()
heap_delete(current, 9)
print(current)  # expected: 12, 7, 9, 3, 6, 8, 2, 1, 0
