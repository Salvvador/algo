class const_time_range:
    def __init__(self, arr):
        self.arr = arr
        self.helper = [0] * (max(arr) + 1)
        for i in range(len(arr)):
            self.helper[arr[i]] += 1
        for i in range(1, len(self.helper)):
            self.helper[i] += self.helper[i - 1]

    def find_range(self, a, b):
        temp = 0
        if a > 0:
            temp = a - 1
        return self.helper[b] - self.helper[temp]


arr1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
ctr = const_time_range(arr1)

print(ctr.find_range(3, 4))
