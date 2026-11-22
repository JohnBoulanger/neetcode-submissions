from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charsInWindow = defaultdict(int)
        windowLength = 0
        maxWindowLength = 0
        l = 0

        for r in range(len(s)):
            windowLength = r - l + 1
            # add character to frequency map
            charsInWindow[s[r]] += 1
                
            # if we have an invalid window, shrink it until its valid
            while windowLength - max(charsInWindow.values()) > k:
                charsInWindow[s[l]] -= 1
                l += 1
                windowLength = r - l + 1

            maxWindowLength = max(windowLength, maxWindowLength)
        return maxWindowLength