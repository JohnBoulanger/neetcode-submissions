from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add new key value pair to store
        self.store[key][timestamp] = value
        # keep track of the timestamps for each key (will be sorted)
        self.timestamps[key].append(timestamp)
        
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timestamps[key]) - 1
        # timestamp less than first timestamp for key
        if not self.timestamps[key] or timestamp < self.timestamps[key][0]:
            return ""
        # binary search to find the value where it matches the largest time <= timestamp
        # for the given key
        while l < r:
            mid = (l + r + 1) // 2
            if self.timestamps[key][mid] == timestamp:
                return self.store[key][timestamp]
            elif self.timestamps[key][mid] < timestamp:
                l = mid
            else:
                r = mid - 1

        return self.store[key][self.timestamps[key][l]]
        
