class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            
            # undershot target, increment left pointer
            if l < r and numbers[l] + numbers[r] < target:
                l += 1
            # overshot target, increment right pointer
            elif l < r and numbers[l] + numbers[r] > target:
                r -= 1
            # target matches, return indices
            else:
                return [l+1, r+1]

        