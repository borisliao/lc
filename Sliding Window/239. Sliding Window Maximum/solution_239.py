from collections import deque
import heapq


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


def review9(nums: list[int], k: int) -> list[int]:
    """
    Mochi 4-14-24
    """
    result = []
    q = deque()
    l = 0
    for r, n in enumerate(nums):
        while q and n > nums[q[-1]]:  # make sure last element in q is the largest
            q.pop()
        q.append(r)

        while q[0] < l:  # make sure first element of the queue is within range of k
            q.popleft()

        if r+1-l == k:  # when the window is at the k length, generate max
            result.append(nums[q[0]])
            l += 1

    return result


def review10(nums: list[int], k: int) -> list[int]:
    """
    Mochi 4-21-24
    """
    result = []
    q = deque()
    l = 0
    for r in range(len(nums)):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        while q[0] < l:
            q.popleft()

        if r+1-l == k:
            l += 1
            result.append(nums[q[0]])

    return result


def review11(nums: list[int], k: int) -> list[int]:
    """
    Mochi 4-24-24
    """
    q = deque()
    result = []
    l = 0
    for r in range(len(nums)):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        while l > q[0]:
            q.popleft()

        if r+1-l == k:
            result.append(nums[q[0]])
            l += 1

    return result


def review12(nums: list[int], k: int) -> list[int]:
    """
    Mochi 6-23-24
    """
    q = deque()
    result = []

    l = 0
    for r in range(len(nums)):
        # remove index if you were able to find a larger number
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove the left most value if we got out of the window
        while l > q[0]:
            q.popleft()

        # if in window
        if r+1-l == k:
            # the largest value is in the beginning of the queue
            result.append(nums[q[0]])
            l += 1

    return result


def review13(nums: list[int], k: int) -> list[int]:
    """
    Mochi 10-16-24
    """
    q = deque()
    result = []

    l = 0
    for r in range(len(nums)):
        while q and nums[r] > nums[q[-1]]:
            q.pop()
        q.append(r)

        while q[0] < l:
            q.popleft()

        if r+1-l == k:
            result.append(nums[q[0]])
            l += 1

    return result
