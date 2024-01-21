from collections import deque


# def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
#     """
#     Slow solution o(n*k)
#     """
#     l = 0
#     r = k
#     result = []

#     while r <= len(nums):
#         vals = nums[l:r]
#         result.append(max(vals))
#         l += 1
#         r += 1
#     return result

# def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
#     l = 0
#     r = k - 1
#     stack = [max(nums[l:r+1])]
#     result = [stack[-1]]

#     while r < len(nums):
#         if nums[l-1] == stack[-1]:
#             stack.pop()
#         if nums[r] > stack[-1]:
#             stack.append(nums[r])

#         result.append(stack[-1])
#         l += 1
#         r += 1

#     return result


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    Anki 1-20-24
    """
    result = []
    q = deque()

    l = 0
    r = 0
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if r+1 >= k:
            result.append(nums[q[0]])
            l += 1
        r += 1

    return result


def review1(nums: list[int], k: int) -> list[int]:
    """
    Anki 1-20-24
    """
    q = deque()

    l = 0
    r = 0

    result = []

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:  # s1 <
            q.popleft()

        if r+1 >= k:  # s1 r < k
            # s1 q.append(r)
            result.append(nums[q[0]])
            l += 1
        r += 1

    return result

# def review2(nums: list[int], k: int) -> list[int]:
#     """
#     Anki 1-20-24
#     """
