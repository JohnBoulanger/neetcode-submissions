class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        res = 0
        
        curEnd = float("-inf")

        for start, end in sortedIntervals:
            # remove overlapping interval that extends furthest
            if start < curEnd:
                res += 1
                # if our current interval reaches further, we want to remove it
                # as its more likely to remove overlap other intervals
                if curEnd > end:
                    curEnd = end
            # not overlapping, start checking intervals in front of it
            else:
                curEnd = end

        return res