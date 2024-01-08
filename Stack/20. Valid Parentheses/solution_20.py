def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
            continue

        stack_val = stack.pop() if stack else None

        if (
            stack_val == '(' and c == ')' or
            stack_val == '{' and c == '}' or
            stack_val == '[' and c == ']'
        ):  # d2 flipped strings
            continue
        else:
            return False

    return True if stack == [] else False  # d1, d2


def review1(s: str) -> bool:
    """
    Anki 1-7-24
    Used: debugger 2
    Time: 15 min
    """
    stack = []
    for c in s:
        # d1 boolean logic (c == '}' or c == ')' or c == ']')
        if (c == '}' or c == ')' or c == ']') and stack == []:
            return False
        if c == '}':
            if stack.pop() != '{':
                return False
        elif c == ')':
            if stack.pop() != '(':
                return False
        elif c == ']':
            if stack.pop() != '[':
                return False
        else:
            stack.append(c)

    return True if stack == [] else False  # d2 check if stack is empty


# def review2(s: str) -> bool:
#     """
#     Anki
#     Added map
#     """
#     Map = {")": "(", "]": "[", "}": "{"}
