'''
Write pseudocode for the brute-force method of solving the maximum-subarray problem. Your procedure should run in Θ(n2)
time.
'''

def max_subarray_brute_force(arr):
    biggest_sum = 0
    left = 0
    right = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if biggest_sum < current_sum:
                left = i
                right = j
                biggest_sum = current_sum
    return biggest_sum, left, right


arr1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
arr2 = [5, 3, 6, 1]
arr3 = [-3, 3, 4, -11]

print(max_subarray_brute_force(arr1))  # 43, 7, 10
print(max_subarray_brute_force(arr2))  # 15, 0, 3
print(max_subarray_brute_force(arr3))  # 7, 1, 2
