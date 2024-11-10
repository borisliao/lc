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


def review4(heights: list[int]) -> int:
    """
    Anki 1-28-24
    Time: > 20 min
    Used: Debugger 3, Solution 3
    """
    stack = []
    H = 0

    for i, h in enumerate(heights):
        l = i  # d6 cant reassign i so will make l
        while stack and stack[-1][0] > h:  # d2  stack and
            h2, i2 = stack.pop()
            H = max(H, h2 * (i-i2))  # s1 ()
            l = i2
        stack.append((h, l))  # d3 ()

    while stack:
        h2, i2 = stack.pop()
        H = max(H, h2*(len(heights)-i2))  # s4 -1-i2, s5 ()

    return H


def review5(heights: list[int]) -> int:
    """
    Anki 1-28-24
    Time: 9:25
    Used: Debugger 2
    """
    stack = []
    area = 0
    for r, h in enumerate(heights):
        l = r
        while stack and stack[-1][0] > h:
            height, l = stack.pop()
            area = max(area, height*(r-l))
        stack.append((h, l))

    for h, l in stack:  # d2 l, h
        area = max(area, h*(len(heights)-l))  # d1 len(height)

    return area


def review6(heights: list[int]) -> int:
    """
    Anki 1-29-24
    Time: 9 min
    Used: Solution 2
    """
    stack = []
    area = 0

    for r in range(len(heights)):
        l = r
        while stack and stack[-1][0] > heights[r]:
            h, l = stack.pop()
            area = max(area, (r-l)*h)  # s2 +1
        stack.append((heights[r], l))  # s1 ()

    for h, l in stack:
        area = max(area, (len(heights)-l)*h)

    return area


def review7(heights: list[int]) -> int:
    """
    Anki 2-3-24
    Used: debugger 2
    Time: 10:42
    """
    largest = 0
    stack = []

    for r, h in enumerate(heights):
        l = r
        while stack and stack[-1][1] > h:
            l, height = stack.pop()
            largest = max(largest, (r-l)*height)
        stack.append((l, h))  # d1 stack.append(l, h)

    for l, h in stack:  # d2 enumerate(stack)
        largest = max(largest, (len(heights)-l)*h)
    return largest


def review8(heights: list[int]) -> int:
    """
    Mochi 4-30-24
    Used: Solution 1
    Time: 40 min
    """
    area = 0
    stack = []

    for i, h in enumerate(heights):
        l = i  # for now
        while stack and stack[-1][1] > h:
            l, height = stack.pop()
            area = max(area, (i-l)*height)
        stack.append((l, h))
        # if h >= prev:
        #     stack.append((i, h))
        #     prev = h
        # else:
        #     while stack and h < prev:
        #         distance, prev = stack.pop()
        #         area = max(prev*(i+1-distance), area)

    for i, h in stack:  # d2 enumerate(stack)
        area = max(area, h*(len(heights)-i))

    return area


def review9(heights: list[int]) -> int:
    """
    Mochi 10-13-24
    """
    stack = []
    result = 0
    for i, h in enumerate(heights):
        l = i
        while stack and stack[-1][1] > h:
            l, height = stack.pop()
            result = max(result, height * (i-l))
        stack.append((l, h))

    for i, h in stack:
        result = max(result, h*(len(heights)-i))

    return result


def review10(heights: list[int]) -> int:
    """
    Mochi 10-17-24
    """
    stack = []
    result = 0

    for i, h in enumerate(heights):
        l = i
        while stack and stack[-1][1] > h:
            l, height = stack.pop()
            result = max(result, height * (i-l))
        stack.append((l, h))

    for i, h in stack:
        result = max(result, h*(len(heights)-i))

    return result


def review11(heights: list[int]) -> int:
    """
    Mochi 11-10-24
    """
    stack = []
    result = 0
    for i in range(len(heights)):
        l = i
        while stack and stack[-1][1] > heights[i]:
            l, height = stack.pop()
            result = max(result, height*(i-l))
        stack.append((l, heights[i]))

    for i, h in stack:
        result = max(result, h*(len(heights)-i))

    return result
