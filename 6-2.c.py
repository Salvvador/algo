def d_arry_heap_extract_max(arr, d):
    arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
    value = arr.pop()
    d_arry_heapify(arr, d, 0)
    return value


def d_arry_heapify(arr, d, i):
    largest = i
    for j in range(i * 2 + 1, i * 2 + d):
        if j < len(arr) and arr[j] > arr[largest]:
            largest = j
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        d_arry_heapify(arr, d, largest)


arr0 = [19, 17, 18, 11, 10, 6, 9, 16, 10, 7, 5, 2]
d_arry_heap_extract_max(arr0, 3)
print(arr0)  # expected: 18, 17, 9, 11, 10, 6, 2, 16, 10, 7, 5
