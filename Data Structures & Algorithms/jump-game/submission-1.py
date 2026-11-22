class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy backwards
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            jump = nums[i]
            if i + jump >= goal:
                goal = i

        return goal == 0