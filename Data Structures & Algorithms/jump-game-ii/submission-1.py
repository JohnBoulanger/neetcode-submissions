class Solution:
    def jump(self, nums: List[int]) -> int:
        # keep track of an array where the number represents how many jumps
        # away you are from the goal and work backwards
        goal = len(nums) - 1
        jumpsAway = [float("inf") for _ in nums]

        if len(nums) == 1:
            return 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                jumpsAway[i] = 1
            elif nums[i] == 0:
                jumpsAway[i] == float("inf")
            else:
                jumpsAway[i] = min(jumpsAway[i : nums[i] + i + 1]) + 1

        return jumpsAway[0]
