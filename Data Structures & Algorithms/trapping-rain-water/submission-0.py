class Solution:
    def trap(self, height: List[int]) -> int:

        amount = 0

        # compute an array that stores the talest bar left of i
        tallestLeft = [0]
        tallestLeftMax = 0
        for h in height:
            tallestLeftMax = max(h, tallestLeftMax)
            tallestLeft.append(tallestLeftMax)
            
        # do the same for the right side, reverse it because we are appending
        tallestRight = [0]
        tallestRightMax = 0
        for h in range(len(height) - 1, -1, -1):
            tallestRightMax = max(height[h], tallestRightMax)
            tallestRight.append(tallestRightMax)
        
        tallestRight.reverse()

        # amount of water we can hold in bar i = 
        # max(0, min(tallest wall left, tallest wall right) - current wall i))
        for i in range(len(height)):
            amount += max(0, min(tallestLeft[i], tallestRight[i]) - height[i])

        return amount
        
