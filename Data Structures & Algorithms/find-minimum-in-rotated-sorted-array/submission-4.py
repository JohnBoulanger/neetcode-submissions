class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high: 
            mid = (high + low) // 2
            # num between greater, start to the right of mid
            if nums[mid] > nums[high]:
                low = mid + 1
            # mid less than right, so smallest value is left of midpoint since start not
            # between mid and r
            else:
                high = mid

        return nums[low]
