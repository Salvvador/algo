def get_nth_fib_numbers(n):
    mem_table = [0, 1, 1]
    if n < len(mem_table):
        return mem_table[n]
    for i in range(3, n + 1):
        mem_table.append(mem_table[i - 1] + mem_table[i - 2])
    return mem_table[n]


print(get_nth_fib_numbers(1))  # expected 1
print(get_nth_fib_numbers(4))  # expected 3
print(get_nth_fib_numbers(9))  # expected 34
print(get_nth_fib_numbers(20))  # expected 6765

