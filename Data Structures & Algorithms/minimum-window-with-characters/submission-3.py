from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount = defaultdict(int)
        tCount = defaultdict(int)
        minLength = float("inf")
        result = ""

        # build counter for t
        for c in t:
            tCount[c] += 1

        l = 0
        have, need = 0, len(tCount)
        for r, c in enumerate(s):
            # grow the window for s and update character counts
            sCount[c] += 1
            # have need
            if sCount[c] == tCount[c]:
                have += 1
            while have == need:
                length = (r - l) + 1
                # update the result if its the smallest substring so far
                if length < minLength:
                    minLength = length
                    result = s[l : (r + 1)]
                sCount[s[l]] -= 1
                # no longer meeting tCount
                if sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return result


