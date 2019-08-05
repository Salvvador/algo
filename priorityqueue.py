import math


class SimplePriorityQueue:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.arr = arr
        self.build_max_heap()

    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        biggest = i
        if left < len(self.arr) and self.arr[left] > self.arr[biggest]:
            biggest = left
        if right < len(self.arr) and self.arr[right] > self.arr[biggest]:
            biggest = right
        if biggest != i:
            self.arr[biggest], self.arr[i] = self.arr[i], self.arr[biggest]
            self.heapify(biggest)

    def build_max_heap(self):
        for i in range(math.floor(len(self.arr) / 2), -1, -1):
            self.heapify(i)

    def heap_maximum(self):
        return self.arr[0]

    def extract_max(self):
        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]
        max_value = self.arr.pop()
        self.heapify(0)
        return max_value

    def print_queue(self):
        print(self.arr[0:len(self.arr)])

    def get_parent(self, i):
        return math.floor((i - 1) / 2);

    def increase_key(self, i, new_value):
        if new_value < self.arr[i]:
            raise ValueError("new value has to be higher then current value")
        self.arr[i] = new_value
        parent = self.get_parent(i)
        while parent >= 0 and self.arr[parent] < new_value:
            self.arr[i] = self.arr[parent]
            i = parent
            parent = self.get_parent(i)
        self.arr[i] = new_value

    def insert(self, new_value):
        self.arr.append(float("-inf"))
        self.increase_key(len(self.arr) - 1, new_value)


if __name__ == '__main__':
    test_arr = [5, 1, 3, 10, 2, 7, 0]

    priority_queue = SimplePriorityQueue(test_arr)
    priority_queue.print_queue()  # expected 10, 5, 7, 1, 2, 3, 0

    print(priority_queue.heap_maximum())  # expected 10
    priority_queue.print_queue()  # expected 10, 5, 7, 1, 2, 3, 0

    print(priority_queue.extract_max())  # expected 10
    priority_queue.print_queue()  # expected 5, 7, 1, 2, 3, 0

    priority_queue.increase_key(3, 10)
    priority_queue.print_queue()  # expected 10, 7, 3, 5, 2, 0

    priority_queue.insert(6)
    priority_queue.print_queue()  # expected 10, 7, 6, 5, 2, 0, 3

    priority_queue.insert(16)
    priority_queue.print_queue()  # expected 16, 10, 6, 7, 2, 0, 3, 5
