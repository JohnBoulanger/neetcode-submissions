class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        # find point at which slow and fast overlap due to cycle
        # value at i in nums is where you go to next
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: # point to same node
                break
    
        # the cycle entrance has two incoming pointers (two indices with that value), so the entrance is the duplicate
        entry = 0
        while True:
            slow = nums[slow]
            entry = nums[entry]
            if slow == entry: # point to same node, duplicate is the index itself because it pointed them there.
                break

        return entry