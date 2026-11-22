class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # keep monotonic increasing stack
        # when we find a value smaller than the head, remove
        # all values from the end of the stack larger than cur
        # where their area is their height * (idx small - idx)

        stack = []
        largestArea = 0

        for i, h in enumerate(heights):
            # update stack to keep it monotonic if we find a value smaller than the 
            # top of the stack
            minIdx = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                # compute the largest area we can make for this bar we are removing
                largestArea = max(largestArea, height * (i - idx))
                minIdx = idx

            stack.append((minIdx, h))

        # compute rectangles for bars remaining on the stack
        for i, h in stack:
            largestArea = max(largestArea, h * (len(heights) - i))

        return largestArea
