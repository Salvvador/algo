# I'm assuming that maps cannot be used it this exercise


def does_sum_exist(arr, x):
    arr.sort()
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == x:
            return True
        if arr[i] + arr[j] < x:
            i = i + 1
        else:
            j = j - 1
    return False


arr1 = [5, 3, 6, 1, 3, 2, 5, 6]
arr2 = [5, 3, 6, 1, 3, 2, 5, 6, 9]

print(does_sum_exist(arr1, 10))  # True
print(does_sum_exist(arr2, 15))  # True
print(does_sum_exist(arr1, 15))  # False
print(does_sum_exist(arr2, 1))  # False
