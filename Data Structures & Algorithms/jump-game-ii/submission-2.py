class Solution:
    def jump(self, nums: List[int]) -> int:
        levels = 0
        l, r = 0, 0
        end = len(nums) - 1

        while r < end:
            # from all the numbers we can jump to currently (l to r) 
            # which jump will give us the furthest jump next
            farthest = max(nums[i] + i for i in range(l, r + 1))
            l, r = r + 1, farthest
            levels += 1
        
        return levels
