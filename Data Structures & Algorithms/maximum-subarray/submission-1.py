class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curSum = 0

        for num in nums:
            curSum += num
            best = max(best, curSum)
            if curSum < 0:
                curSum = 0

        return best