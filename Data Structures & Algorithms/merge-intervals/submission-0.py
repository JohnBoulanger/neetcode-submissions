class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        curStart, curEnd = sortedIntervals[0]

        res = []

        for start, end in sortedIntervals:
            # this interval cant merge with our current one, start a new one
            if start > curEnd:
                res.append([curStart, curEnd])
                curStart, curEnd = start, end
            # otherwise this interval overlaps with the current one, merge it by growing its end
            # start doesnt change because we sorted the intervals by their start time initially
            else:
                curEnd = max(curEnd, end)
        
        # append last remaining interval weve been building
        res.append([curStart, curEnd])

        return res

            
        