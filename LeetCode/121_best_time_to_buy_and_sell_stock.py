from typing import List

# def maxProfit(prices: List[int]) -> int:
#     temp_diff = 0
#     for day in range(1, len(prices)):
#         for prev_day in range(0, day):
#             if (prices[day] - prices[prev_day]) > temp_diff:
#                 temp_diff = prices[day] - prices[prev_day]
#     return temp_diff


def maxProfit(prices: List[int]) -> int:
    min_price = min(prices)
    max_price = max(prices[prices.index(min_price):])
    return max_price - min_price


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
