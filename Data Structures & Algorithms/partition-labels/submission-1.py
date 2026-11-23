from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = defaultdict(int)

        # create a dict that stores the last idx for each char in s
        for i, c in enumerate(s):
            last[c] = i

        res = []
        lastIdx = last[s[0]]
        start = 0

        for i, c in enumerate(s):
            # last value of current char
            lastIdx = max(lastIdx, last[c])
            # reached end of all characters within substring, add to result
            if i == lastIdx:
                res.append(i - start + 1)
                start = i + 1

        return res



