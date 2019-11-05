def top_down_rod_cutting_with_cost(prices, length, cost):
    mem_table = [0] * length
    return top_down_rod_cutting_with_cost_help(prices, length, cost, mem_table)


def top_down_rod_cutting_with_cost_help(prices, length, cost, mem_table):
    if mem_table[length - 1] != 0:
        return mem_table[length - 1]
    highest = prices[length - 1] - cost
    for i in range(1, length):
        temp = top_down_rod_cutting_with_cost_help(prices, i, cost, mem_table) + \
               top_down_rod_cutting_with_cost_help(prices, length - i, cost, mem_table)
        if temp > highest:
            highest = temp
    mem_table[length - 1] = highest
    return highest


t_prices = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]
print(top_down_rod_cutting_with_cost(t_prices, 1, 0.2))  # expected: 0.8

print(top_down_rod_cutting_with_cost(t_prices, 2, 0.2))  # expected: 4.8

print(top_down_rod_cutting_with_cost(t_prices, 4, 0.2))  # expected: 9.6

print(top_down_rod_cutting_with_cost(t_prices, 9, 0.2))  # expected: 24.6
