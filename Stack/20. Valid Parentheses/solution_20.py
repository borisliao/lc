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

    return True  # d1


# def review1(s: str) -> bool:
#     """
#     Anki
#     """
#     pass
