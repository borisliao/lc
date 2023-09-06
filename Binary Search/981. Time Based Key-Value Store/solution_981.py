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
