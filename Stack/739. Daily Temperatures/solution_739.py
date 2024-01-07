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
