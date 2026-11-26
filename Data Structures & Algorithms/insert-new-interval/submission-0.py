class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        res, i, n = [], 0, len(intervals)
        newStart, newEnd = newInterval
        # add initial intervals that wont merge with new one
        while i < n and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1
        
        # interval can merge with currently growing one until
        # we find an interval whose start doesnt overlap with the growing end
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(intervals[i][0], newStart)
            newEnd = max(intervals[i][1], newEnd)
            i += 1

        res.append([newStart, newEnd])
        res.extend(intervals[i:])
        return res
