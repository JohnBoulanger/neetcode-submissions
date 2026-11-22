class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = []

        for i in range(len(sortedNums)):
            # skip if weve already done two sum II on this num (same as prev) to skip dupes
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            # do two sum II to find target
            target = 0 - sortedNums[i]
            l, r = i + 1, len(sortedNums) - 1
            
            while l < r:
                if sortedNums[l] + sortedNums[r] < target:
                    l += 1
                elif sortedNums[l] + sortedNums[r] > target:
                    r -= 1
                else:
                    result.append([sortedNums[i], sortedNums[r], sortedNums[l]])
                    l += 1
                    # skip numbers that are the same as matching l to avoid duplicates
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1

        return result