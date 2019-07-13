'''
Implement both the brute-force and recursive algorithms for the maximum-subarray problem on your own computer. What
problem size n0 gives the crossover point at which the recursive algorithm beats the brute-force algorithm? Then,
change the base case of the recursive algorithm to use the brute-force algorithm whenever the problem size is less than
n0. Does that change the crossover point?
'''

import math
import random
import time


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


def max_subarray_recursive(arr):
    mid = math.floor(len(arr) / 2)
    left_sum, left_left, left_right = max_subarray_recursive_step(arr, 0, mid)
    right_sum, right_left, right_right = max_subarray_recursive_step(arr, mid + 1, len(arr) - 1)
    crossing_sum, crossing_left, crossing_right = max_subarray_crossing(arr, 0, mid, len(arr) - 1)
    if left_sum >= right_sum and left_sum >= crossing_sum:
        return left_sum, left_left, left_right
    if crossing_sum >= right_sum and crossing_sum >= left_sum:
        return crossing_sum, crossing_left, crossing_right
    return crossing_sum, crossing_left, crossing_right


def max_subarray_recursive_step(arr, left, right):
    if left == right:
        return arr[left], left, right
    mid = math.floor((right - left) / 2) + left
    left_sum, left_left, left_right = max_subarray_recursive_step(arr, left, mid)
    right_sum, right_left, right_right = max_subarray_recursive_step(arr, mid + 1, right)
    crossing_sum, crossing_left, crossing_right = max_subarray_crossing(arr, left, mid, right)
    if left_sum >= right_sum and left_sum >= crossing_sum:
        return left_sum, left_left, left_right
    if crossing_sum >= right_sum and crossing_sum >= left_sum:
        return crossing_sum, crossing_left, crossing_right
    return right_sum, right_left, right_right


def max_subarray_crossing(arr, left, mid, right):
    crossing_sum_left = 0
    crossing_left = mid
    current = 0
    for i in range(mid, left - 1, -1):
        current += arr[i]
        if current > crossing_sum_left:
            crossing_left = i
            crossing_sum_left = current
    crossing_sum_right = 0
    crossing_right = mid
    current = 0
    for i in range(mid + 1, right + 1):
        current += arr[i]
        if current > crossing_sum_right:
            crossing_right = i
            crossing_sum_right = current
    return crossing_sum_right + crossing_sum_left, crossing_left, crossing_right


testArr = []
recursive_time = 0
brute_force_time = 0
while brute_force_time >= recursive_time:
    testArr.append(random.randint(-100, 100))
    start = time.time()
    max_subarray_brute_force(testArr)
    end = time.time()
    brute_force_time = end - start
    start = time.time()
    max_subarray_brute_force(testArr)
    end = time.time()
    recursive_time = end - start

print('Crossover point at which brute force is slower: ' + str(len(testArr)))
