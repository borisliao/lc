import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    """
    Anki 2-7-24
    Time: 6 min
    """
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return nums[0]


def review1(nums: list[int], k: int) -> int:
    """
    Anki 2-8-24
    Time: 4 min
    Used: https://www.youtube.com/watch?v=AzDs7qV1ugA
    """
    heap = []

    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def review2(nums: list[int], k: int) -> int:
    """
    Anki 2-8-24
    Time: 2 min
    Used: https://www.youtube.com/watch?v=AzDs7qV1ugA
    """
    heap = []

    for n in nums:
        if len(heap) < k:
            heapq.heappush(heap, n)
        elif n > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, n)

    return heap[0]
