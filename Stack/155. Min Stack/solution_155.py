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


def review1():
    """
    Anki 1-8-24
    Time: 10 min
    """

    class MinStack:

        def __init__(self):
            self.stack = []
            self.minimum_at_index = {}
            self.minimum = float('inf')

        def push(self, val: int) -> None:
            self.minimum_at_index[len(self.stack)] = self.minimum
            self.minimum = min(self.minimum, val)
            self.stack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.minimum = self.minimum_at_index[len(self.stack)]

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.minimum

    return MinStack()


def review2():
    """
    1-8-24
    Time: (10 min) + 3 min
    Used 2 stacks instead of 1 stack and 1 hash
    """

    class MinStack:

        def __init__(self):
            self.stack = []
            self.last_minimum = []
            self.minimum = float('inf')

        def push(self, val: int) -> None:
            self.last_minimum.append(self.minimum)
            self.minimum = min(self.minimum, val)
            self.stack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.minimum = self.last_minimum.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.minimum

    return MinStack()


def review3():
    """
    Anki 1-22-24
    Time: 9 min
    """
    class MinStack:

        def __init__(self):
            self.stack = []
            self.next_min = [float('inf')]

        def push(self, val: int) -> None:
            self.stack.append(val)
            self.next_min.append(min(self.next_min[-1], val))

        def pop(self) -> None:
            self.stack.pop()
            self.next_min.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.next_min[-1]

    return MinStack()


# def review4():
#     """
#     Anki 1-22-24
#     Time: 9 min
#     """
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
