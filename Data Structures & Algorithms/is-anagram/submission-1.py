from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(list(s))
        tCount = Counter(list(t))

        return True if sCount == tCount else False
        