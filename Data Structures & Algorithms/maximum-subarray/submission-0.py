class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        # can never be above 0 since the initial prefix sum is 0
        smallestPrefixSum = 0
        prefixSum = 0
        for num in nums:
            # store current prefix sum
            prefixSum += num
            # best subarray we can find up to the value num in nums is our current
            # prefix sum chopping off the smallest prefix sum we've found
            best = prefixSum - smallestPrefixSum
            # update if new best, or smallest prefix found so far
            res = max(best, res)
            smallestPrefixSum = min(prefixSum, smallestPrefixSum)

        return res
            
