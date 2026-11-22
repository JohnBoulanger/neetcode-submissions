class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = num we need to get target with value at nums[i] where the value is i
        need = {}
        # iterate over all nums
        for i in range(len(nums)):
            # if the current number matches a target number we need, return the indeces
            if nums[i] in need:
                return [need[nums[i]], i]
            need[target - nums[i]] = i

        return []

        