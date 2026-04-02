class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.store[key]) > 0:
            # find highest key that safisfies key <= timestamp
            l, r = 0, len(self.store[key]) - 1
            res = ""
            while l <= r:
                mid = (l + r) // 2
                if self.store[key][mid][0] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
            return self.store[key][r][1] if r >= 0 else ""
        else:
            return ""