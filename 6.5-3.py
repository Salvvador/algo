import math


class SimpleMinQueue:
    def __init__(self, arr):
        self.heap_size = len(arr)
        self.arr = arr.copy()
        self.build_min_heap()

    def heap_minimum(self):
        return self.arr[0]

    def heap_extract_min(self):
        minimum = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        self.min_heapify(0)
        return minimum

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < self.heap_size and self.arr[smallest] > self.arr[left]:
            smallest = left
        if right < self.heap_size and self.arr[smallest] > self.arr[right]:
            smallest = right
        if smallest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[smallest]
            self.arr[smallest] = temp
            self.min_heapify(smallest)

    def heap_decrease_key(self, i, key):
        if self.arr[i] < key:
            raise
        self.arr[i] = key
        while i > 0 and self.arr[i] < self.arr[self.get_parent(i)]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.get_parent(i)]
            self.arr[self.get_parent(i)] = temp
            i = self.get_parent(i)

    def get_parent(self, i):
        return math.floor((i - 1) / 2)

    def min_heap_insert(self, key):
        self.heap_size += 1
        self.arr.append(math.inf)
        self.heap_decrease_key(self.heap_size - 1, key)

    def build_min_heap(self):
        for i in range(math.floor(self.heap_size / 2), -1, -1):
            self.min_heapify(i)

    def print_min_queue(self):
        print(self.arr[0:self.heap_size])


test_arr = [5, 1, 3, 10, 2, 7, 0]

min_queue = SimpleMinQueue(test_arr)
min_queue.print_min_queue()  # expected 0, 1, 3, 10, 2, 7, 5

print(min_queue.heap_minimum())  # expected 0
min_queue.print_min_queue()  # expected 0, 1, 3, 10, 2, 7, 5

print(min_queue.heap_extract_min())  # expected 0
min_queue.print_min_queue()  # expected 1, 2, 3, 10, 5, 7

min_queue.heap_decrease_key(3, 0)
min_queue.print_min_queue()  # expected 0, 1, 3, 2, 5, 7

min_queue.min_heap_insert(-1)
min_queue.print_min_queue()  # expected -1, 1, 0, 2, 5, 7, 3
