class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # calculate running product for numbers left of nums[i]
        prodL = 1
        prodR = 1
        prodLArr = []
        result = []
        for num in nums:
            result.append(prodL)
            prodL *= num

        # multiply product of values left of nums[i] by values right of nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= prodR
            prodR *= nums[i]
           
        return result