def largestRectangleArea(heights: list[int]) -> int:
    """
    Anki 1-15-24
    Used: [Largest Rectangle in Histogram - Leetcode 84 - Python](https://www.youtube.com/watch?v=zx5Sw9130L0)
    Time: 1h
    """
    largest = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:  # s1 < largest
            index, height = stack.pop()
            largest = max(largest, (i - index) * height)
            start = index
        stack.append((start, h))

    width = len(heights)  # d2 height
    for i, h in stack:
        largest = max(largest, (width - i)*h)  # d3 i-width

    return largest


def review1(heights: list[int]) -> int:
    """
    Anki 1-15-24
    """
    stack = []
    largest = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            largest = max(largest, (i-index) * height)
            start = index
        stack.append((start, h))

    for i, h in stack:  # s1, d2 enumerate
        largest = max(largest, (len(heights)-i) * h)  # s1

    return largest


# def review2(heights: list[int]) -> int:
#     """
#     Anki 1-21-24
#     Brute force
#     Time: 8:25
#     """
#     area = 0

#     for l in range(len(heights)):
#         for r in range(l, len(heights)):
#             area = max(area, min(heights[l:r+1]) * (r+1-l))

#     return area


def review3(heights: list[int]) -> int:
    """
    Anki 1-21-24
    Time: 40 min
    """
    area = 0
    stack = []

    for r in range(len(heights)):
        l = r  # s1 down 2
        while stack and stack[-1][1] > heights[r]:  # s2 stack[0][1]
            i, v = stack.pop()
            area = max(area, v*(r-i))
            l = i
        stack.append((l, heights[r]))

    for i, v in stack:
        area = max(area, v*(len(heights)-i))  # d1 (i+1-l)

    return area

# def review4(heights: list[int]) -> int:
#     """
#     Anki 1-19-24
#     """
#     pass
