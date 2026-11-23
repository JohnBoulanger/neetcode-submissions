class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        firstLast = {}

        # create a dict of tuples where we have the index of the first and last character for each c in s
        for i, c in enumerate(s):
            if c in firstLast:
                first, last = firstLast[c]
                firstLast[c] = (first, i)
            else:
                firstLast[c] = (i, i) 

        res = []
        last = firstLast[s[0]][1]
        start = 0

        for i, c in enumerate(s):
            # last value of current char
            last = max(last, firstLast[c][1])
            # reached end of all characters within substring, add to result
            if i == last:
                res.append(i - start + 1)
                start = i + 1

        return res



