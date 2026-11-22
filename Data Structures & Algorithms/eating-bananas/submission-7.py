class Solution:

    def eatBananasInTime(self, piles: List[int], h: int, k: int) -> bool:
        t = 0
        for p in piles:
            t += (p + k - 1) // k

        return True if t <= h else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2
            if self.eatBananasInTime(piles, h, mid):
                r = mid
            else:
                l = mid + 1
            
        return l


    