class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0
        # iterate over all unique numbers in the array
        for num in unique_nums:
            length = 0
            # if its the start of a new sequence, find its length
            if num - 1 not in unique_nums:
                while num in unique_nums:
                    num += 1
                    length += 1

                longest = max(longest, length)
                            
        return longest

        