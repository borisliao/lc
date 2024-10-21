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


def review2(height: list[int]) -> int:
    """
    Anki 1-16-24
    Used: [Trapping Rain Water - Google Interview Question - Leetcode 42](https://www.youtube.com/watch?v=ZI2z5pq0TqA)
    Time: 10 min
    """
    l, r = 0, len(height) - 1
    max_left, max_right = height[l], height[r]
    result = 0

    while l < r:
        if max_left <= max_right:
            l += 1
            max_left = max(max_left, height[l])
            result += max_left - height[l]  # s1 min(max_left, max_right)
        else:
            r -= 1
            max_right = max(max_right, height[r])
            result += max_right - height[r]  # s1 min(max_left, max_right)

    return result


def review3(height: list[int]) -> int:
    """
    Anki 1-22-24
    Time: 54 min
    Used: Solution 3
    """
    result = 0
    l = 0
    r = len(height) - 1
    left_max = height[l]  # s1
    right_max = height[r]  # s1

    while l < r:
        if left_max < right_max:  # s2 height[l] < height[r]
            l += 1
            left_max = max(height[l], left_max)  # s1
            result += left_max - height[l]  # s1, s3  min(left_max, right_max)
        elif left_max >= right_max:  # s2 height[l] >= height[r]
            r -= 1
            right_max = max(height[r], right_max)  # s1
            result += right_max - height[r]  # s1
    return result


def review4(height: list[int]) -> int:
    """
    Anki 1-22-24
    """
    l, r = 0, len(height) - 1
    lMax, rMax = height[l], height[r]
    result = 0

    while l < r:
        if lMax < rMax:
            l += 1
            lMax = max(lMax, height[l])
            result += lMax - height[l]
        else:
            r -= 1
            rMax = max(rMax, height[r])
            result += rMax - height[r]  # s1 -=

    return result


def review5(height: list[int]) -> int:
    """
    Anki 1-26-24
    Used: Debugger 4
    Time: 13 min
    """
    result = 0
    maxL = 0
    maxR = 0

    l = 0
    r = len(height) - 1  # d3 len(height)

    while l < r:
        if height[l] < height[r]:
            maxL = max(maxL, height[l])
            l += 1
            result += (maxL - height[l]) if maxL - height[l] > 0 else 0
        else:
            maxR = max(maxR, height[r])
            r -= 1  # d4 +=
            result += (maxR - height[r]) if maxR - height[r] > 0 else 0
    return result


def review6(height: list[int]) -> int:
    """
    Anki 1-29-24
    Time: 5:41
    """
    l = 0
    r = len(height) - 1
    maxL = height[l]
    maxR = height[r]
    water = 0

    while l < r:
        if height[l] < height[r]:
            l += 1
            maxL = max(maxL, height[l])
            water += maxL - height[l]
        else:
            r -= 1
            maxR = max(maxR, height[r])
            water += maxR-height[r]

    return water


def review7(height: list[int]) -> int:
    """
    Anki 2-6-24
    Time: 12 min
    """
    max_left = []
    max_right = []

    l = 0
    for h in height:
        l = max(l, h)
        max_left.append(l)

    r = 0
    for h in reversed(height):
        r = max(r, h)
        max_right.append(r)
    max_right = max_right[::-1]

    result = 0
    for i, h in enumerate(height):
        result += (min(max_left[i], max_right[i]) - h)
    return result


def review8(height: list[int]) -> int:
    """
    2-6-24
    """
    l = 0
    r = len(height) - 1
    result = 0
    maxL = height[l]
    maxR = height[r]

    while l < r:
        if height[l] < height[r]:
            maxL = max(maxL, height[l])
            l += 1
            result += max(0, maxL-height[l])
        else:
            maxR = max(maxR, height[r])
            r -= 1
            result += max(0, maxR-height[r])
    return result


def review9(height: list[int]) -> int:
    """
    Mochi 4-14-24
    """
    l = 0
    r = len(height) - 1
    maxL = height[l]
    maxR = height[r]
    result = 0

    while l < r:
        if height[l] < height[r]:
            maxL = max(maxL, height[l])
            l += 1
            result += max(0, maxL-height[l])
        else:
            maxR = max(maxR, height[r])
            r -= 1
            result += max(0, maxR-height[r])
    return result


def review10(height: list[int]) -> int:
    """
    Mochi 4-24-24
    """
    l = 0
    r = len(height) - 1

    maxL = 0
    maxR = 0

    water = 0

    while l < r:
        if height[l] < height[r]:
            maxL = max(maxL, height[l])
            water += max(maxL-height[l], 0)
            l += 1
        else:
            maxR = max(maxR, height[r])
            water += max(maxR-height[r], 0)
            r -= 1

    return water


def review11(height: list[int]) -> int:
    """
    Mochi 10-7-24
    Monotonic Stack
    https://medium.com/@w.zhang.pro/monotonic-stack-37e1fe1b0916
    """
    stack = []
    rainWater = 0

    for i, r in enumerate(height):
        while stack and height[stack[-1]] < r:
            bottomBound = stack.pop()
            if stack:
                h = min(r, height[stack[-1]]) - height[bottomBound]
                w = i-stack[-1]-1
                rainWater += h*w
        stack.append(i)

    return rainWater


def review12(height: list[int]) -> int:
    """
    Mochi 10-13-24
    """
    l, r = 0, len(height)-1
    maxL = 0
    maxR = 0
    rainWater = 0

    while l < r:
        if height[l] < height[r]:
            maxL = max(maxL, height[l])
            rainWater += max(maxL-height[l], 0)
            l += 1
        else:
            maxR = max(maxR, height[r])
            rainWater += max(maxR-height[r], 0)
            r -= 1
    return rainWater


def review13(height: list[int]) -> int:
    """
    Mochi 10-15-24
    """
    l = 0
    r = len(height) - 1
    lMax = 0
    rMax = 0
    result = 0

    while l < r:
        lMax = max(lMax, height[l])
        rMax = max(rMax, height[r])
        if height[l] < height[r]:
            result += min(lMax, rMax)-height[l]
            l += 1
        else:
            result += min(lMax, rMax)-height[r]
            r -= 1
    return result


def review14(height: list[int]) -> int:
    """
    Mochi 10-15-24
    Monotonic Stack
    """
    stack = []
    result = 0

    for r, right_hill in enumerate(height):
        while stack and height[stack[-1]] < right_hill:
            valley = stack.pop()
            if stack:
                left_hill = stack[-1]
                water_height = min(
                    right_hill, height[left_hill]) - height[valley]
                width = r - left_hill - 1
                result += water_height*width
        stack.append(r)
    return result


def review15(height: list[int]) -> int:
    """
    Mochi 10-21-24
    """
    l = 0
    r = len(height) - 1
    maxL = 0
    maxR = 0
    result = 0

    while l < r:
        maxL = max(maxL, height[l])
        maxR = max(maxR, height[r])
        if height[l] < height[r]:
            result += min(maxL, maxR)-height[l]
            l += 1
        else:
            result += min(maxL, maxR)-height[r]
            r -= 1

    return result
