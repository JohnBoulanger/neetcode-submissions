class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # define an array where val[i] = product of numbers before i in array
        prefixProd = [1] * len(nums)
        result = [1] * len(nums)
        prod = 1

        for i in range(1, len(nums)):
            prefixProd[i] = prod * nums[i-1]
            prod *= nums[i-1]

        # track product of numbers right of i and multiply that by the numbers left of i
        # which is whats stored in prefixProd[i]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = prod * prefixProd[i]
            prod *= nums[i]

        return result

    
        