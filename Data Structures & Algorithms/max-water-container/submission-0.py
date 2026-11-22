class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        maxArea = 0

        # two pointer approach, move left and right pointers inwards
        # move left pointer if its shortest, move right pointer if its shortest
        # keep track of each area along the way, return the max
        while l < r:
            base = r - l
            area = min(heights[l], heights[r]) * base
            maxArea = max(maxArea, area)

            # left height smaller, move it over
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea
        