import math


def evalRPN(tokens: list[str]) -> int:
    """
    1-5-23
    Used: [Evaluate Reverse Polish Notation - Leetcode 150 - Python](https://www.youtube.com/watch?v=iu0082c4HDE)
    """
    stack = []
    for t in tokens:
        if t not in set(['+', '-', '*', '/']):
            stack.append(int(t))  # d2 stack.append(t)
            continue
        l = stack.pop()
        r = stack.pop()
        if t == "+":
            stack.append(l + r)
        if t == '-':
            stack.append(r - l)
        if t == '*':
            stack.append(l * r)
        if t == "/":
            stack.append(int(r / l))  # i2 / , d3 //, s4 math.floor

    return stack[0]  # s1 result


# def review1(tokens: list[str]) -> int:
#     pass
