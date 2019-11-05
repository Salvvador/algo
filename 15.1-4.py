class RodCutter:
    def __init__(self, prices, fixed_cost):
        self.prices = prices
        self.fixed_cost = fixed_cost
        self.mem_table_value = [0] * len(prices)
        self.mem_table_picks = [0] * len(prices)

    def find_cuts_for_length(self, length):
        value = self.find_cuts_for_length_rec(length)
        cuts = self.get_cuts(length)
        return value, cuts

    def find_cuts_for_length_rec(self, length):
        if self.mem_table_value[length - 1] != 0:
            return self.mem_table_value[length - 1]
        self.mem_table_value[length - 1] = self.prices[length - 1] - self.fixed_cost
        self.mem_table_picks[length - 1] = length
        for i in range(1, length):
            temp = self.find_cuts_for_length_rec(i) + self.find_cuts_for_length_rec(length - i)
            if temp > self.mem_table_value[length - 1]:
                self.mem_table_value[length - 1] = temp
                self.mem_table_picks[length - 1] = i
        return self.mem_table_value[length - 1]

    def get_cuts(self, length):
        cuts = []
        current_cut = length
        while current_cut > 0:
            cuts.append(self.mem_table_picks[current_cut - 1])
            current_cut = current_cut - self.mem_table_picks[current_cut - 1]
        return cuts


t_prices = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]
rodCutter = RodCutter(t_prices, 0.2)
print(rodCutter.find_cuts_for_length(1))  # expected: 0.8, [1]

print(rodCutter.find_cuts_for_length(2))  # expected: 4.8, [2]

print(rodCutter.find_cuts_for_length(4))  # expected: 9.6, [2, 2]

print(rodCutter.find_cuts_for_length(9))  # expected: 24.6, [3, 6]
