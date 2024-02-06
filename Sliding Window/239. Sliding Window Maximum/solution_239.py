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
#     Anki 1-21-24
#     Brute force
#     Time: 8 min
#     Used: debugger 1
#     """
#     l = 0
#     result = []

#     for r in range(k, len(nums)+1):  # d1 +1
#         result.append(max(nums[l:r]))
#         l += 1

#     return result


def review3(nums: list[int], k: int) -> list[int]:
    """
    Anki 1-21-24
    Time: 20 min
    Used: debugger 1
    """
    l = 0
    result = []

    q = deque()

    for r in range(len(nums)):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if q[0] < l:
            q.popleft()

        if r+1-l >= k:
            result.append(nums[q[0]])  # d1 result.append(q[0])
            l += 1

    return result


def review4(nums: list[int], k: int) -> list[int]:
    """
    Anki 1-27-24
    Time: 20 min
    Used: Solution 1
    """
    q = deque()
    l = 0
    result = []
    for r in range(len(nums)):
        while q and nums[q[-1]] < nums[r]:  # s1 q[-1] < nums[r]
            q.pop()
        q.append(r)  # s1 r

        if r+1-l < k:
            continue

        result.append(nums[q[0]])  # s1 nums[q[-1]]
        if l > q[0]:  # s1 q[0] == nums[l]
            q.popleft()
        l += 1

    return result


def review5(nums: list[int], k: int) -> list[int]:
    """
    Anki 1-27-24
    Used: Debugger 1
    Time: 8 min
    """
    q = deque()
    result = []
    l = 0

    for r in range(len(nums)):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if r+1-l < k:
            continue

        if q[0] < l:
            q.popleft()
        result.append(nums[q[0]])
        l += 1

    return result  # d1


def review6(nums: list[int], k: int) -> list[int]:
    """
    Anki 1-29-24
    Time: 12 min
    Used: Solution 1
    """
    stack = deque()
    result = []
    l = 0

    for r, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:  # s2 stack and
            stack.pop()
        stack.append(r)

        if stack[0] < l:
            stack.popleft()

        if r+1-l >= k:  # s1 < len(nums)
            result.append(nums[stack[0]])
            l += 1

    return result


def review7(nums: list[int], k: int) -> list[int]:
    """
    Anki 2-6-24
    Time: 15 min
    Used: Solution 1
    """
    result = []
    q = deque()
    l = 0
    for r, n in enumerate(nums):
        while q and n > nums[q[-1]]:
            q.pop()
        q.append(r)

        while q[0] < l:
            q.popleft()

        if r+1-l == k:
            result.append(nums[q[0]])  # s1 q[0]
            l += 1

    return result
