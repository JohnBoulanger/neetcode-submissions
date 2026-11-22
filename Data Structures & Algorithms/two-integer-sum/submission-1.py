class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = num we need to get target with value at nums[i] where the value is i
        targetList = {}
        # iterate over all nums
        for i in range(len(nums)):
            # if the current number matches a target number we need, return the indeces
            if nums[i] in targetList:
                return [targetList[nums[i]], i]
            targetList[target - nums[i]] = i

        return []

        