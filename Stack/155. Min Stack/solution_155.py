def minStack():
    """
    1-3-24
    Time: 30 min
    Used: Debugger 2
    """
    class MinStack:

        def __init__(self):
            self.min = float('inf')  # d1 float('-inf')
            self.lookup = {}
            self.stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            self.lookup[(val, len(self.stack))] = self.min
            self.min = min(self.min, val)

        def pop(self) -> None:
            val = self.stack.pop()  # d2 val, length
            # d2 (val, length)
            self.min = self.lookup[(val, len(self.stack) + 1)]
            del self.lookup[(val, len(self.stack) + 1)]  # d2 (val, length)

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min

    return MinStack()


# def minStack():
#     class MinStack:

#         def __init__(self):
#             pass

#         def push(self, val: int) -> None:
#             pass

#         def pop(self) -> None:
#             pass

#         def top(self) -> int:
#             pass

#         def getMin(self) -> int:
#             pass

#     return MinStack()
