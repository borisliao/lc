import heapq


def lastStoneWeight(stones: list[int]) -> int:
    """
    Anki 2-4-24
    Used: Solution
    Time: 19 min
    """
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) >= 2:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if y-x < 0:
            heapq.heappush(stones, y-x)
    return -stones[0] if stones else 0


def review1(stones: list[int]) -> int:
    """
    Anki 2-5-24
    Used: debugger 2
    Time: 5:34
    """
    stones = [-i for i in stones]
    heapq.heapify(stones)

    while len(stones) >= 2:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if y-x < 0:  # d2 >
            heapq.heappush(stones, y-x)
    return -stones[0] if stones else 0  # d1 -


def review2(stones: list[int]) -> int:
    """
    Anki 2-5-24
    Time: 3:08
    """
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) >= 2:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if y < x:
            heapq.heappush(stones, y-x)
    return -stones[0] if stones else 0
