# def maxArea(height: list[int]) -> int:
#     """
#     Anki 1-15-24
#     Used: [Container with Most Water - Leetcode 11 - Python](https://www.youtube.com/watch?v=UuiTKBwPgAo)
#     Brute Force Solution
#     """
#     largest = 0
#     for l in range(len(height)):
#         for r in range(l + 1, len(height)):  # s1 l + 1
#             # d1 parentheses r-l
#             largest = max(largest, min(height[l], height[r]) * (r- l))

#     return largest

def maxArea(height: list[int]) -> int:
    """
    Anki 1-15-24
    Used: [Container with Most Water - Leetcode 11 - Python](https://www.youtube.com/watch?v=UuiTKBwPgAo)
    """
    largest = 0
    l = 0
    r = len(height) - 1
    while l < r:
        largest = max(largest, min(height[l], height[r]) * (r - l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return largest
