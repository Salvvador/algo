'''
Use the following ideas to develop a nonrecursive, linear-time algorithm for the maximum-subarray problem. Start at the
left end of the array, and progress toward the right, keeping track of the maximum subarray seen so far. Knowing a
maximum subarray A[1..j], extend the answer to find a maximum subarray ending at index j+1 by using the following
observation: a maximum subarray A[i..j+1], for some 1≤i≤j+1. Determine a maximum subarray of the form A[i..j+1] in
constant time based on knowing a maximum subarray ending at index j.
'''


def max_subarray_linear_time(arr):
    max_sum = arr[0]
    max_left = 0
    max_right = 0
    current_max_sum = arr[0]
    current_max_sum_left = 0
    for i in range(1, len(arr)):
        current = arr[i]
        if current_max_sum < 0:
            current_max_sum_left = i
            current_max_sum = 0
        current_max_sum += current
        if current_max_sum > max_sum:
            max_left = current_max_sum_left
            max_right = i
            max_sum = current_max_sum
    return max_sum, max_left, max_right


arr1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
arr2 = [5, 3, 6, 1]
arr3 = [-3, 3, 4, -11]
arr4 = [13, -3, -25, 20, -3, -16, -23, 100, -20, -7, 12, -5, -22, 15, -4, 7]

print(max_subarray_linear_time(arr1))  # 43, 7, 10
print(max_subarray_linear_time(arr2))  # 15, 0, 3
print(max_subarray_linear_time(arr3))  # 7, 1, 2
print(max_subarray_linear_time(arr4))  # 100, 7, 7
