class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        # iterate over all heights
        for i, height in enumerate(heights):
            # keep monotonic stack (increasing)
            # if we run into a value smaller than the top, pop off all values larger than the
            # current height
            # and compute their max height which would be where that height we are popping started
            # until now, so h(popped) * (i(current) - start_idx(where h was)), save max area
            minStart = i
            while stack and stack[-1][1] > height:
                (start_idx, h) = stack.pop()
                area = h * (i - start_idx)
                maxArea = max(area, maxArea)
                minStart = start_idx
            stack.append((minStart, height))

        # check remaining items on the stack, they stretch from where they started to the 
        # end because they are still on the stack and have nothing smaller than them
        # in front of them
        for i, height in stack:
            area = height * (len(heights) - i)
            maxArea = max(area, maxArea)
        
        return maxArea
