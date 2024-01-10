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


def review1(tokens: list[str]) -> int:
    """
    Anki 1-5-23
    Time: 5 min
    Used: debugger 1, insight 1
    """
    s = []
    for t in tokens:
        if t == '+':
            s.append(s.pop() + s.pop())
        elif t == '-':  # d1 if
            l, r = s.pop(), s.pop()
            s.append(r - l)
        elif t == '*':  # d1 if
            s.append(s.pop() * s.pop())
        elif t == '/':  # d1 if
            l, r = s.pop(), s.pop()
            s.append(int(r/l))  # i1 l/r
        else:
            s.append(int(t))

    return s[0]


def review2(tokens: list[str]) -> int:
    """
    Anki 1-10-23
    Time: 14 min
    Used: Debugger 3
    """
    stack = []
    for t in tokens:
        if t == '+':
            stack.append(stack.pop() + stack.pop())
        elif t == '-':
            r, l = stack.pop(), stack.pop()
            stack.append(l - r)
        elif t == '*':
            # d3 stack.append(stack.append(...))
            stack.append(stack.pop() * stack.pop())
        elif t == '/':
            r, l = stack.pop(), stack.pop()
            # d1 int(l / r), d2 stack.append(stack.append(...))
            stack.append(int(l / r))
        else:
            stack.append(int(t))

    return stack[0]
