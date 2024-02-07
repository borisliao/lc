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
