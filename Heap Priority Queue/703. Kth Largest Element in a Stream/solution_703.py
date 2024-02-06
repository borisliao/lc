import heapq


# def KthLargest():
#     class KthLargest:

#         def __init__(self, k: int, nums: list[int]):
#             self.heap = nums
#             self.k = k
#             heapq.heapify(self.heap)

#         def add(self, val: int) -> int:
#             heapq.heappush(self.heap, val)
#             return self.heap

#     return KthLargest

def KthLargest():
    """
    Anki 1-31-24
    Used: Debugger 1
    """
    class KthLargest:

        def __init__(self, k: int, nums: list[int]):
            self.k = k
            self.heap = nums  # d1 []
            heapq.heapify(self.heap)
            while len(self.heap) > self.k:
                heapq.heappop(self.heap)

        def add(self, val: int) -> int:
            heapq.heappush(self.heap, val)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
            return self.heap[0]

    return KthLargest


def review1():
    """
    Anki 2-6-24
    Time: 20 min
    Used: Solution 1
    """
    class KthLargest:

        def __init__(self, k: int, nums: list[int]):
            self.h = nums
            self.k = k
            heapq.heapify(self.h)

        def add(self, val: int) -> int:
            heapq.heappush(self.h, val)  # s1 heapq.heappush(val)
            while len(self.h) > self.k:
                heapq.heappop(self.h)
            return self.h[0]  # s1 heapq.nlargest(self.k, self.h)

    return KthLargest

# def review2():
#     class KthLargest:

#         def __init__(self, k: int, nums: list[int]):

#         def add(self, val: int) -> int:

#     return KthLargest
