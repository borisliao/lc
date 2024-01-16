def trap3n(height: list[int]) -> int:
    """
    Anki 1-16-24
    Used: [Trapping Rain Water - Google Interview Question - Leetcode 42](https://www.youtube.com/watch?v=ZI2z5pq0TqA)
    Complexity: time O(4n) space: o(3n)
    Did not use two pointers
    Time: 10 min
    """
    max_left = []
    largest = 0
    for h in height:
        largest = max(largest, h)
        max_left.append(largest)

    max_right = [0] * len(height)
    largest = 0
    i = len(height) - 1
    while i >= 0:
        largest = max(largest, height[i])
        max_right[i] = largest
        i -= 1

    result = []
    for i, h in enumerate(height):
        water = min(max_left[i], max_right[i]) - h
        result.append(water if water >= 0 else 0)

    return sum(result)


# def trap(height: list[int]) -> int:
#     """
#     Anki 1-16-24
#     Used: [Trapping Rain Water - Google Interview Question - Leetcode 42](https://www.youtube.com/watch?v=ZI2z5pq0TqA)
#     Complexity: time O(n), space o(n)
#     """
#     l = 0
#     r = len(height) - 1
#     result = 0

#     while l <= r:
#         water = 0
#         if height[l] <= height[r]:
#             l += 1
#             water = min(height[l], height[r]) - height[l]
#             result += max(0, water)
#         else:
#             r -= 1
#             water = min(height[l], height[r]) - height[r]
#             result += max(0, water)

#     return result

def trap(height: list[int]) -> int:
    """
    Anki 1-16-24
    Used: [Trapping Rain Water - Google Interview Question - Leetcode 42](https://www.youtube.com/watch?v=ZI2z5pq0TqA)
    Complexity: time O(n), space o(n)
    """
    l = 0
    r = len(height) - 1
    max_left = height[l]
    max_right = height[r]
    result = 0

    if not height:
        return 0

    while l < r:
        if max_left <= max_right:
            l += 1
            max_left = max(max_left, height[l])
            result += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            result += max_right - height[r]

    return result


def review1(height: list[int]) -> int:
    """
    Anki 1-16-24
    Used: debugger 2
    Time: 9:09
    """
    l, r = 0, len(height) - 1
    max_left, max_right = height[l], height[r]
    result = 0

    while l < r:
        if max_left < max_right:
            l += 1
            # d2 max(0,
            result += max(0, min(max_left, max_right) - height[l])
            max_left = max(max_left, height[l])
        else:
            r -= 1
            # d2 max(0,
            result += max(0, min(max_left, max_right) - height[r])
            # d1 max(max_left, max_right)
            max_right = max(max_right, height[r])

    return result


# def review2(height: list[int]) -> int:
#     """
#     Anki 1-16-24
#     Used: [Trapping Rain Water - Google Interview Question - Leetcode 42](https://www.youtube.com/watch?v=ZI2z5pq0TqA)
#     """
