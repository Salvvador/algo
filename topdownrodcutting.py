def top_down_rod_cutting(prices, length):
    mem_table = [0] * length
    return top_down_rod_cutting_rec(prices, length, mem_table)


def top_down_rod_cutting_rec(prices, length, mem_table):
    if mem_table[length - 1] != 0:
        return mem_table[length - 1]
    highest = prices[length - 1]
    for i in range(1, length):
        temp = top_down_rod_cutting_rec(prices, length - i, mem_table) + top_down_rod_cutting_rec(prices, i, mem_table)
        if temp > highest:
            highest = temp
    mem_table[length - 1] = highest
    return highest


t_prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(top_down_rod_cutting(t_prices, 1))  # expected: 1

print(top_down_rod_cutting(t_prices, 2))  # expected: 5

print(top_down_rod_cutting(t_prices, 4))  # expected: 10

print(top_down_rod_cutting(t_prices, 9))  # expected: 25
