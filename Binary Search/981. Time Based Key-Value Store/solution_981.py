# def naive():
#     class TimeMap:
#         def __init__(self):
#             self.k = {}

#         def set(self, key: str, value: str, timestamp: int) -> None:
#             self.k[key] = self.k.get(key, {}) | {timestamp: value}

#         def get(self, key: str, timestamp: int) -> str:
#             if key in self.k:
#                 for i in range(timestamp, -1, -1):
#                     if i in self.k[key]:
#                         return self.k[key][i]

#             return ''

#     return TimeMap()

# def halfBinarySearch():
#     class TimeMap:
#         def __init__(self):
#             self.k = {}

#         def set(self, key: str, value: str, timestamp: int) -> None:
#             self.k[key] = self.k.get(key, {}) | {timestamp: value}

#         def get(self, key: str, timestamp: int) -> str:
#             if key in self.k:
#                 ts = sorted(self.k[key].keys())

#                 l, r = 0, len(ts) - 1
#                 potential = -1
#                 while l <= r:
#                     m = (l + r) // 2

#                     if ts[m] > timestamp:
#                         r = m - 1
#                     elif ts[m] < timestamp:
#                         l = m + 1
#                         potential = ts[m]
#                     else:
#                         return self.k[key][timestamp]

#                 if potential != -1:
#                     return self.k[key][potential]
#             return ''

#     return TimeMap()

# def binarySearchAttempt():
#     """
#     This solution is still too slow for test_lc_44.py
#     """
#     class TimeMap:
#         def __init__(self):
#             self.k = {}
#             self.ts = {}

#         def set(self, key: str, value: str, timestamp: int) -> None:
#             self.k[key] = self.k.get(key, {}) | {timestamp: value}
#             self.ts[key] = self.ts.get(key, [])

#             #  this binary insertion is broken
#             # l, r = 0, len(self.ts[key]) - 1

#             # while l <= r:
#             #     m = (l + r) // 2

#             #     if self.ts[key][m] > timestamp:
#             #         l = m + 1
#             #     elif self.ts[key][m] < timestamp:
#             #         r = m - 1
#             #     else:
#             #         return

#             # self.ts[key].insert(abs(l+r), timestamp)

#             import bisect
#             bisect.insort(self.ts[key], timestamp)

#         def get(self, key: str, timestamp: int) -> str:
#             if key in self.k:
#                 ts = self.ts[key]

#                 l, r = 0, len(ts) - 1
#                 potential = -1
#                 while l <= r:
#                     m = (l + r) // 2

#                     if ts[m] > timestamp:
#                         r = m - 1
#                     elif ts[m] < timestamp:
#                         l = m + 1
#                         potential = ts[m]
#                     else:
#                         return self.k[key][timestamp]

#                 if potential != -1:
#                     return self.k[key][potential]
#             return ''

#     return TimeMap()

from collections import defaultdict


def neetCode():
    """
    https://www.youtube.com/watch?v=fu2cD_6E8Hw
    """
    class TimeMap:
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.keyStore = {}  # key : list of [val, timestamp]

        def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.keyStore:
                self.keyStore[key] = []
            self.keyStore[key].append([value, timestamp])

        def get(self, key: str, timestamp: int) -> str:
            res, values = "", self.keyStore.get(key, [])
            l, r = 0, len(values) - 1
            while l <= r:
                m = (l + r) // 2
                if values[m][1] <= timestamp:
                    res = values[m][0]
                    l = m + 1
                else:
                    r = m - 1
            return res

    return TimeMap()


# def binarySearchWithDict():
#     class TimeMap:
#         def __init__(self):
#             self.k = {}

#         def set(self, key: str, value: str, timestamp: int) -> None:
#             self.k[key] = self.k.get(key, {}) | {timestamp: value}

#         def get(self, key: str, timestamp: int) -> str:
#             # converting to list is a o(n) opperation
#             res, values = "", list(self.k.get(key, {}))
#             l, r = 0, len(values) - 1
#             while l <= r:
#                 m = (l + r) // 2
#                 if values[m] <= timestamp:
#                     res = self.k[key][values[m]]
#                     l = m + 1
#                 else:
#                     r = m - 1
#             return res

#     return TimeMap()

def review1():
    """
    Anki 12-3-23
    Used: Peak at solution (2)
    Time: 43:12
    """
    class TimeMap:
        def __init__(self):
            self.keyStore = defaultdict(lambda: [])  # s1

        def set(self, key: str, value: str, timestamp: int) -> None:
            self.keyStore[key].append([timestamp, value])

        def get(self, key: str, timestamp: int) -> str:
            values = self.keyStore[key]
            result = ""  # s3

            l = 0
            r = len(values) - 1

            while l <= r:
                m = (l + r) // 2

                if values[m][0] <= timestamp:
                    result = values[m][1]  # s2, s4
                    l = m + 1  # s3
                else:
                    r = m - 1  # s3

            return result

    return TimeMap()


def review2():
    """
    Anki 12-3-23
    Used: Debugger (1) 
    Time: 18:00
    """
    class TimeMap:
        def __init__(self):
            self.values_of = defaultdict(lambda: [])

        def set(self, key: str, value: str, timestamp: int) -> None:
            self.values_of[key].append([timestamp, value])

        def get(self, key: str, timestamp: int) -> str:
            key_values = self.values_of[key]
            result = ""

            l = 0
            r = len(key_values) - 1

            while l <= r:
                m = (l + r) // 2
                if timestamp >= key_values[m][0]:  # d1
                    result = key_values[m][1]
                    l = m + 1
                else:
                    r = m - 1

            return result

    return TimeMap()


def review2():
    """
    Anki 12-3-23
    Time: 12:04
    """
    class TimeMap:
        def __init__(self):
            self.key_store = defaultdict(lambda: [])

        def set(self, key: str, value: str, timestamp: int) -> None:
            self.key_store[key].append(
                {"timestamp": timestamp, "value": value})

        def get(self, key: str, timestamp: int) -> str:
            li = self.key_store[key]

            l = 0
            r = len(li) - 1

            closest_timestamp = ''

            while l <= r:
                m = (l + r) // 2

                if li[m]["timestamp"] == timestamp:
                    return li[m]["value"]

                if li[m]["timestamp"] < timestamp:
                    closest_timestamp = li[m]["value"]
                    l = m + 1
                else:
                    r = m - 1

            return closest_timestamp

    return TimeMap()


def review3():
    """
    Anki 12-31-23
    Time: 20 min
    Basic itteration version (no binary search)
    """
    class TimeMap:
        def __init__(self):
            self.store = defaultdict(lambda: {})

        def set(self, key: str, value: str, timestamp: int) -> None:
            self.store[key][timestamp] = value

        def get(self, key: str, timestamp: int) -> str:
            if key in self.store:
                if timestamp in self.store[key]:
                    return self.store[key][timestamp]
                for time, value in reversed(self.store[key].items()):
                    if time > timestamp:
                        continue
                    return value
            return ''

    return TimeMap()


# def review4():
#     """
#     Anki 12-31-23
#     Due to the nested dictionary instead of list, the time complexity is o(n) instead of o(log(n))
#     Used: debugger 4
#     Time: 35 min
#     """
#     class TimeMap:
#         def __init__(self):
#             self.store = defaultdict(lambda: {})

#         def set(self, key: str, value: str, timestamp: int) -> None:
#             self.store[key][timestamp] = value

#         def get(self, key: str, timestamp: int) -> str:
#             if key in self.store:
#                 if timestamp in self.store[key]:
#                     return self.store[key][timestamp]

#             kv = list(self.store[key].items())  # d2, d4 conversion is slow
#             l = 0  # d1 indent out of "if key"
#             r = len(kv) - 1
#             largest = None
#             while l <= r:
#                 m = (l+r)//2
#                 # d2 self.store, d3 m in self.store[key]
#                 if kv[m][0] < timestamp:
#                     largest = kv[m][1]
#                     l = m + 1  # d2 l = t
#                 else:
#                     r = m - 1

#             return largest if largest else ''

#     return TimeMap()

# def review5():
#     """
#     Anki
#     """
#     class TimeMap:
#         def __init__(self):
#             pass

#         def set(self, key: str, value: str, timestamp: int) -> None:
#             pass

#         def get(self, key: str, timestamp: int) -> str:
#             pass

#     return TimeMap()
