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


def review3():
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


def review4():
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


def review5():
    """
    Anki 1-21-24
    """
    class TimeMap:
        def __init__(self):
            self.store: dict[str, list[tuple[int, str]]] = {}

        def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.store:  # d1
                self.store[key] = []  # d1
            self.store[key].append((timestamp, value))

        def get(self, key: str, timestamp: int) -> str:
            values = self.store[key]
            l = 0
            r = len(values)-1

            min_val = ""
            while l <= r:
                m = (l+r)//2
                if values[m][0] < timestamp:
                    min_val = values[m][1]
                    l = m + 1  # s3 l +=1
                elif values[m][0] > timestamp:
                    r = m - 1
                else:
                    return values[m][1]
            return min_val  # d2

    return TimeMap()


def review6():
    """
    Mochi 4-10-24
    Time: 30 min
    """
    class TimeMap:
        def __init__(self):
            self.db = {}

        def set(self, key: str, value: str, timestamp: int) -> None:
            if key in self.db:
                self.db[key].append([value, timestamp])
            else:
                self.db[key] = [[value, timestamp]]  # d1

        def get(self, key: str, timestamp: int) -> str:
            db_vals = self.db[key]
            closest_match = ''  # d2 None
            l = 0
            r = len(db_vals) - 1
            while l <= r:
                m = (l+r)//2
                if db_vals[m][1] == timestamp:
                    return db_vals[m][0]
                if db_vals[m][1] > timestamp:
                    r = m - 1
                else:
                    closest_match = db_vals[m][0]
                    l = m + 1
            return closest_match

    return TimeMap()


def review7():
    """
    Mochi 10-23-24
    """
    class TimeMap:
        def __init__(self):
            self.store = {}

        def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.store:
                self.store[key] = []
            self.store[key].append((value, timestamp))

        def get(self, key: str, timestamp: int) -> str:
            l = 0
            r = len(self.store.get(key, [])) - 1

            res = ""

            while l <= r:
                m = (l+r)//2
                if self.store[key][m][1] == timestamp:
                    return self.store[key][m][0]

                if self.store[key][m][1] < timestamp:
                    res = self.store[key][m][0]
                    l = m + 1
                else:
                    r = m - 1

            return res

    return TimeMap()

# def review():
#     """
#     Mochi 10-23-24
#     """
#     class TimeMap:
#         def __init__(self):
#             pass

#         def set(self, key: str, value: str, timestamp: int) -> None:
#             pass

#         def get(self, key: str, timestamp: int) -> str:
#             pass

#     return TimeMap()
