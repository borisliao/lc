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


def review4(temperatures: list[int]) -> list[int]:
    """
    Anki 1-14-24
    Time: 40 min
    Used: solution 1, debugger 1
    """
    result = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:  # d1 <
            index = stack.pop()
            result[index] = i-index
        stack.append(i)

    return result


def review5(temperatures: list[int]) -> list[int]:
    """
    Anki 1-16-24
    Time: 3 min
    """
    result = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i-index
        stack.append(i)
    return result


def review6(temperatures: list[int]) -> list[int]:
    """
    Anki 1-19-24
    Time: 20 min
    """
    stack = []
    result = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:  # d1 len(stack) >= 2
            index = stack.pop()
            result[index] = i-index
        stack.append(i)  # d1 down3

    return result


def review7(temperatures: list[int]) -> list[int]:
    """
    Anki 1-20-24
    Time: 16 min
    Used: Solution 1
    """
    result = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:  # s1 if and >
            index = stack.pop()
            result[index] = i-index
        stack.append(i)
    return result


def review8(temperatures: list[int]) -> list[int]:
    """
    Anki 1-20-24
    Time: 5 min
    Used: debugger 1
    """
    stack = []
    result = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:  # d1 stack[-1]
            index = stack.pop()
            result[index] = i-index
        stack.append(i)

    return result


def review9(temperatures: list[int]) -> list[int]:
    """
    Anki 1-22-24
    """
    result = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:  # d1 >
            index = stack.pop()
            result[index] = i-index
        stack.append(i)
    return result


def review10(temperatures: list[int]) -> list[int]:
    """
    Anki 1-22-24
    Time: 5 min
    """
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            index = stack.pop()
            result[index] = i-index
        stack.append(i)

    return result
