from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = min(prices[0:len(prices)-1]) if len(prices) > 1 else prices[0]
    max_price = max(prices[prices.index(min_price):])
    return max_price - min_price


print(maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(maxProfit([7, 6, 4, 3, 1]) == 0)
print(maxProfit([2, 4, 1]) == 2)
print(maxProfit([1]) == 0)
print(maxProfit([2, 1, 4]) == 3)
print(maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2)
print(maxProfit([3, 2, 6, 5, 0, 3]) == 4)
