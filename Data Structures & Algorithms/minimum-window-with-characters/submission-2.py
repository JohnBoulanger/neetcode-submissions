from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        dictT = Counter(t)
        dictS = defaultdict(int)
        l = 0
        minLength = float('inf')

        have, need = 0, len(dictT)   # chars covered so far vs chars that need covering

        for r in range(len(s)):
            # add new character to window dict
            c = s[r]
            dictS[c] += 1
            # this char just reached the count t needs (that char is valid)
            if c in dictT and dictS[c] == dictT[c]:
                have += 1

            # while the window covers t, record it and shrink
            while have == need:
                length = r - l + 1
                if length < minLength:
                    minLength = length
                    result = s[l : r + 1]
                # remove the left char
                c = s[l]
                dictS[c] -= 1
                # this char just dropped below what t needs (invalid window)
                if c in dictT and dictS[c] < dictT[c]:
                    have -= 1
                l += 1

        return result