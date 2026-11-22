from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        q.append((nums[0], 0))
        # fill queue
        for i in range(1, k):
            # add to top of queue if new largest
            if nums[i] >= q[-1][0]:
                q.append((nums[i], i))
            else:
            # otherwise add to back of queue, remove smaller numbers at the left end
            # of the queue until you find one bigger
                while nums[i] > q[0][0]:
                    q.popleft()
                q.appendleft((nums[i], i))

        result = [q[-1][0]]

        for i in range(k, len(nums)):
            # same as above
            if nums[i] >= q[-1][0]:
                q.append((nums[i], i))
            else:
                while nums[i] > q[0][0]:
                    q.popleft()
                q.appendleft((nums[i], i))

            # grab largest valid value from top of queue
            while q[-1][1] < (i - k + 1):
                q.pop()

            result.append(q[-1][0])

        return result

