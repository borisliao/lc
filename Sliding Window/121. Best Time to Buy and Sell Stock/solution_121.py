from typing import List


def maxProfit(prices: List[int]) -> int:
    max = 0
    min = prices[0]

    maxProfit = 0

    for i in prices:
        if i < min:
            min = i
            max = i
        elif i > max:
            max = i

        if maxProfit < max-min:
            maxProfit = max-min

    return maxProfit
