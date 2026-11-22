class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while  l <= r:
            mid = (l + r) // 2
            # move l
            if nums[mid] < target:
                l = mid + 1
            # move r
            elif nums[mid] > target:
                r = mid - 1
            # found val
            else:
                return mid

        return -1
        
        