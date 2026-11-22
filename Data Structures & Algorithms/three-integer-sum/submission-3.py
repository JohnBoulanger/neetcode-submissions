class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        result = []

        # two pointer approach
        for i in range(n):
            # skip any values that we already used to determine the target
            # since the previous copy already searched everything to its right
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # find two numbers in the array that sum to target using two pointer approach
            # between i and the end because any values before i have already been checked
            # for triplets
            target = 0 - nums[i]
            l, r = i + 1, n - 1

            while l < r:
                # undershooting target, increment left
                if nums[l] + nums[r] < target:
                    l += 1
                # overshooting target, decrement right
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    # if triplet doesnt share indices, add it to the list of solutions
                    if i != l and i != r and l != r:
                        result.append([nums[i], nums[l], nums[r]])
                        # keep checking for more triplets
                        l += 1
                        # skip any values that match the l triplet we just used
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        
        return result


        




        