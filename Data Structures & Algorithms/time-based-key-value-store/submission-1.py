from collections import defaultdict

class TimeMap:

    def __init__(self):
        # each key has a list of pairs which is (word, timestamp)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        # binary search to find timestamp at boundary of largest timestamp <= timestamp parameter
        items = self.store[key]
        if not items or items[0][1] > timestamp: return ""
        # timestamps in items array are naturally increasing since they are literal "timestamps"
        res = ""

        l, r = 0, len(items) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if items[mid][1] == timestamp:
                return items[mid][0]
            elif items[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid

        return items[l][0]

