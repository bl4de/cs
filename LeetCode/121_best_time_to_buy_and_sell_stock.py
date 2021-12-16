from typing import List


def max_profit(prices: List[int]) -> int:
    temp_diff = 0
    for day in range(1, len(prices)):
        for prev_day in range(0, day):
            if (prices[day] - prices[prev_day]) > temp_diff:
                temp_diff = prices[day] - prices[prev_day]
    return temp_diff


print(max_profit([7, 1, 5, 3, 6, 4]) == 5)
print(max_profit([7, 6, 4, 3, 1]) == 0)
