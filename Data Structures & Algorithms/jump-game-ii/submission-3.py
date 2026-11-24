class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # shortest and furthest we can jump from 0
        l, r = 0, 0
        jumps = 0
        goal = len(nums) - 1

        while r < goal:
            # track farthest we can jump at jump i
            farthest = r
            # for all numbers within our jump range, whats the furthest we can leap
            # from those values we can jump to now?
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            # check all values we didnt try up to the new furthest we can jump to
            l = r + 1
            r = farthest
            jumps += 1

        return jumps
