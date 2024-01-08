def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    Anki 1-7-24
    Used: [Daily Temperatures - Monotonic Stack - Leetcode 739 - Python](https://www.youtube.com/watch?v=cTBiBSnjO3c)
    """
    result = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = (i - index)
        stack.append(i)
    return result


def review1(temperatures: list[int]) -> list[int]:
    """
    Anki 1-7-24
    """
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        # s1 missing t >
        while stack and t > temperatures[stack[-1]]:
            index = stack.pop()  # s1
            result[index] = i - index
        stack.append(i)

    return result


def review2(temperatures: list[int]) -> list[int]:
    """
    Anki 1-7-24
    Time: 2 min
    """
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)

    return result


def review3(temperatures: list[int]) -> list[int]:
    """
    1-7-24
    https://leetcode.com/problems/daily-temperatures/solutions/397728/easy-python-o-n-time-o-1-extra-space-beat-99-9
    """
    max_temp = 0
    result = [0] * len(temperatures)
    i = len(temperatures) - 1
    while i >= 0:
        if temperatures[i] >= max_temp:
            max_temp = temperatures[i]
        else:
            days = 1
            while temperatures[i] >= temperatures[i+days]:
                days += result[i+days]
            result[i] = days
        i -= 1
    return result
