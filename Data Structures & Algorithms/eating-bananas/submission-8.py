class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        bestRate = max(piles)

        def eatInTime(piles, rate, h):
            t = 0
            for p in piles:
                t += (p + rate - 1) // rate
            return t <= h


        # binary search for best rate
        while low <= high:
            rate = (high + low) // 2
            if eatInTime(piles, rate, h):
                high = rate - 1
                bestRate = rate
            else:
                low = rate + 1

        return bestRate


        