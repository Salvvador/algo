def top_down_rod_cutting(prices, length):
    mem_table = [0] * 10
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


prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(top_down_rod_cutting(prices, 1))  # expected: 1

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(top_down_rod_cutting(prices, 2))  # expected: 5

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(top_down_rod_cutting(prices, 4))  # expected: 10

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(top_down_rod_cutting(prices, 9))  # expected: 10
