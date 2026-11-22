class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # calculate running product for numbers left of nums[i]
        prodL = 1
        prodLArr = []
        prodR = 1
        prodRArr = []
        result = []
        for i in range(len(nums)):
            prodLArr.append(prodL)
            prodRArr.append(prodR)
            prodL *= nums[i]
            prodR *= nums[-(i+1)]

        prodRArr.reverse()
        for i in range(len(nums)):
            result.append(prodLArr[i] * prodRArr[i])

        return result