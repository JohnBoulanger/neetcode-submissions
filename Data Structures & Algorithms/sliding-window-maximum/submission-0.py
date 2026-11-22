import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        # get initial window and store its index too
        window = []
        for i in range(0, k - 1):
            window.append([nums[i], i])

        # turn it into max heap
        heapq.heapify_max(window)

        # move the window and pop the head of the heap until 
        # you find one with an index in the window
        l = 0
        for r in range(k - 1, len(nums)):
            heapq.heappush_max(window, [nums[r], r])
            # pop top of heap until value is in window range
            while window[0][1] < l:
                heapq.heappop_max(window)

            # once you find a value in range its the largest, so add it to the result
            result.append(window[0][0])
            l += 1

        return result
            