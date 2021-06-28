'''
첫 코드 : 시간초과

result = 0
prices = [7, 6, 4, 3, 1]
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        if prices[j] - prices[i] >= result:
            result = prices[j] - prices[i]
print(result)
'''
import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_profit = sys.maxsize

        for price in prices:
            min_profit = min(min_profit, price)
            profit = max(profit, price - min_profit)

        return profit
