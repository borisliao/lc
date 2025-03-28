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


def review4():
    """
    Mochi 4-17-24
    Time: 15 min
    """
    class MinStack:

        def __init__(self):
            self.stack = []
            self.min = []
            self.smallest = None

        def push(self, val: int) -> None:
            self.stack.append(val)
            # d1 not self.smallest (== True when self.smallest = 0)
            if self.smallest == None or self.smallest > val:
                self.smallest = val
            self.min.append(self.smallest)

        def pop(self) -> None:
            self.stack.pop()
            self.min.pop()
            # d2 if self.min else None
            self.smallest = self.min[-1] if self.min else None

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min[-1]

    return MinStack()


def review5():
    """
    Mochi 10-6-24
    """
    class MinStack:

        def __init__(self):
            self.stack = []
            self.min = [float('inf')]

        def push(self, val: int) -> None:
            self.stack.append(val)
            self.min.append(min(val, self.min[-1]))

        def pop(self) -> None:
            self.stack.pop()
            self.min.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min[-1]

    return MinStack()


def review6():
    """
    Mochi 10-13-24
    """
    class MinStack:

        def __init__(self):
            self.stack = []
            self.minStack = [float('inf')]

        def push(self, val: int) -> None:
            self.stack.append(val)
            self.minStack.append(min(self.minStack[-1], val))

        def pop(self) -> None:
            self.stack.pop()
            self.min = self.minStack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.minStack[-1]

    return MinStack()


def review7():
    """
    Mochi 10-20-24
    """
    class MinStack:

        def __init__(self):
            self.stack = []
            self.least = [float('inf')]

        def push(self, val: int) -> None:
            self.stack.append(val)
            if val < self.least[-1]:
                self.least.append(val)
            else:
                self.least.append(self.least[-1])

        def pop(self) -> None:
            self.stack.pop()
            self.least.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.least[-1]

    return MinStack()


def review8():
    """
    Mochi 12-2-24
    """
    class MinStack:

        def __init__(self):
            self.stack = []
            self.min_vals = [float('inf')]

        def push(self, val: int) -> None:
            self.stack.append(val)
            new_min = min(self.min_vals[-1], val)
            self.min_vals.append(new_min)

        def pop(self) -> None:
            self.stack.pop()
            self.min_vals.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_vals[-1]

    return MinStack()


# def review():
#     """
#     Mochi
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
