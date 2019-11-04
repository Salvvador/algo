def bottom_up_rod_cutting(prices, length):
    mem_table = [0] * length
    highest = 0
    for i in range(0, length):
        highest = prices[i]
        for j in range(0, i):
            temp = mem_table[j] + mem_table[i - j - 1]
            if temp > highest:
                highest = temp
        mem_table[i] = highest
    return highest


t_prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(bottom_up_rod_cutting(t_prices, 1))  # expected: 1
print(bottom_up_rod_cutting(t_prices, 2))  # expected: 5
print(bottom_up_rod_cutting(t_prices, 4))  # expected: 10
print(bottom_up_rod_cutting(t_prices, 9))  # expected: 25
