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


def review1(height: list[int]) -> int:
    """
    Anki 1-19-24
    Time: 20 min
    Used: [Container with Most Water - Leetcode 11 - Python](https://www.youtube.com/watch?v=UuiTKBwPgAo)
    """
    l = 0
    r = len(height) - 1
    water = 0
    while l < r:
        # d1 max(water, d2 max(height[l]
        water = max(water, min(height[l], height[r]) * (r-l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return water


def review2(height: list[int]) -> int:
    """
    Anki 1-20-24
    Time: 6 min
    Used: Solution 1
    """
    water = 0
    l = 0
    r = len(height) - 1
    while l < r:
        water = max(water, min(height[l], height[r]) * (r-l))  # s1 r+1
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return water


def review3(height: list[int]) -> int:
    """
    Anki 1-20-24
    Time: 3:30
    """
    l = 0
    r = len(height) - 1
    result = 0

    while l < r:
        result = max(result, min(height[l], height[r]) * (r-l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return result


def review4(height: list[int]) -> int:
    """
    Anki 1-22-24
    Time: 5 min
    Used: Debugger 1
    """
    water = 0
    l, r = 0, len(height) - 1

    while l < r:
        water = max(water, min(height[l], height[r]) * (r-l))  # d1 ()
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return water


def review5(height: list[int]) -> int:
    """
    Anki 1-22-24
    Time: 6 min
    Used: Debugger 1
    """
    water = 0
    l = 0
    r = len(height) - 1
    while l < r:
        water = max(water, min(height[l], height[r]) * (r-l))  # d1 +1
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return water


def review6(height: list[int]) -> int:
    """
    Anki 2-15-24
    """
    result = 0
    l = 0
    r = len(height) - 1

    while l < r:
        result = max(result, min(height[l], height[r])*(r-l))
        if height[r] < height[l]:
            r -= 1
        else:
            l += 1

    return result
