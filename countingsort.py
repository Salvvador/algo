def counting_sort(input_arr):
    max_value = max(input_arr)
    helper_arr = [0] * (max_value + 1)
    output_arr = [0] * len(input_arr)
    for i in range(len(input_arr)):
        helper_arr[input_arr[i]] += 1
    for i in range(1, max_value + 1):
        helper_arr[i] += helper_arr[i - 1]
    for i in range(len(input_arr) - 1, -1, -1):
        output_arr[helper_arr[input_arr[i]] - 1] = input_arr[i]
        helper_arr[input_arr[i]] = helper_arr[input_arr[i]] - 1
    return output_arr


arr1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
arr2 = [4]
arr3 = [5, 4, 3, 2, 1]

print(counting_sort(arr1))
print(counting_sort(arr2))
print(counting_sort(arr3))
