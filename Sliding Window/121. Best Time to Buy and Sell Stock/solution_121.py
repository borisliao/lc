def maxProfit(prices: list[int]) -> int:
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


def review1(prices: list[int]) -> int:
    """
    Anki 12-20-23
    Used: Solution 4
    Time: 29:19
    """
    l = 0  # buy
    r = 1  # sell
    profit = 0

    while r < len(prices):  # s1 <=
        # are we profitable?
        if prices[l] < prices[r]:
            # s2 l-r, s3 r-l, s4 profit[r]-profit[l]
            profit = max(prices[r]-prices[l], profit)
        else:
            l = r
        r += 1
    return profit


def review2(prices: list[int]) -> int:
    """
    Anki 12-20-23
    Time: 13 min
    """
    l = 0
    r = 1

    profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = max(prices[r] - prices[l], profit)
        else:
            l = r
        r += 1
    return profit


def review3(prices: list[int]) -> int:
    """
    Anki 12-25-23
    Time: 21 min
    Used: debugger 1
    """
    l = 0  # buy
    r = 0  # sell
    max_profit = 0
    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
            continue  # d1 break
        max_profit = max(max_profit, prices[r]-prices[l])
        r += 1
    return max_profit


def review4(prices: list[int]) -> int:
    """
    Anki 1-14-24
    Time: 4:30
    """
    l = 0  # buy
    max_profit = 0

    for r in range(len(prices)):  # sell
        if prices[l] > prices[r]:
            l = r
            continue
        max_profit = max(max_profit, prices[r] - prices[l])

    return max_profit


def review5(prices: list[int]) -> int:
    """
    Mochi 4-18-24
    Time: 8:22
    """
    profit = 0
    l = 0
    for r in range(len(prices)):
        if l == r:
            continue
        while l < r and prices[l] >= prices[r]:
            l += 1
        profit = max(prices[r]-prices[l], profit)

    return profit


def review6(prices: list[int]) -> int:
    """
    Mochi 10-9-24
    """
    result = 0
    l = 0
    for r in range(len(prices)):
        if l != r:
            profit = prices[r] - prices[l]
            result = max(profit, result)

        while l < r and prices[l] > prices[r]:
            l += 1

    return result
