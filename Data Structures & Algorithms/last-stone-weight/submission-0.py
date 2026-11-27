import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        # max heap, largest stones at the top
        heapq.heapify(h)

        while len(h) > 1:
            s1 = -heapq.heappop(h)
            s2 = -heapq.heappop(h)
            # add the negative of the difference between the two largest stones back in the heap
            heapq.heappush(h, -abs(s1 - s2))

        # return what remains
        return -h[0]