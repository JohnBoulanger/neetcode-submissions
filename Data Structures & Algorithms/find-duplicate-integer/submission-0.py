class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use floyds detection algorithm slow and fast
        # slow and fast are indexes
        slow = 0
        fast = 0

        # if there is a duplicate, there will be a cycle, wait until indicies overlap
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 2nd phase to find start of cycle, steps to go back to cycle for start = steps to walk to entrance of
        # cycle for entry
        entry = 0
        while entry != slow:
            slow = nums[slow]
            entry = nums[entry]

        return entry
        