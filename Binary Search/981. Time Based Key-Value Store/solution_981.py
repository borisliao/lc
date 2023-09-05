def naive():
    class TimeMap:
        def __init__(self):
            self.k = {}

        def set(self, key: str, value: str, timestamp: int) -> None:
            self.k[key] = self.k.get(key, {}) | {timestamp: value}

        def get(self, key: str, timestamp: int) -> str:
            if key in self.k:
                for i in range(timestamp, -1, -1):
                    if i in self.k[key]:
                        return self.k[key][i]

            return ''

    return TimeMap()
