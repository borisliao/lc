import heapq
import math


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Anki 2-5-24
    Time: 15 min
    """
    distances = []

    for x, y in points:
        d = abs(math.sqrt(math.pow(x, 2) + math.pow(y, 2)))  # d1 , 2
        heapq.heappush(distances, (d, (x, y)))  # d3 -d

    result = []
    for _ in range(k):  # d2 len(k)
        d, point = heapq.heappop(distances)
        result.append(list(point))

    return result
