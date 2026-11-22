class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        # create a counter for s1 and slide a window over s2 until there is a match
        # otherwise false
        target = {}
        for ch in s1:
            target[ch] = target.get(ch, 0) + 1

        # build initial counter of size len(s1) for permutation tracking
        counter = {}
        for i in range(len(s1)):
            counter[s2[i]] = counter.get(s2[i], 0) + 1
        for r in range(len(s1), len(s2)):
            # if there is a match, return true
            if counter == target:
                return True
            
            # otherwise update the windows counter
            if counter[s2[r - len(s1)]] > 1:
                counter[s2[r - len(s1)]] -= 1
            else:
                del counter[s2[r - len(s1)]]
            counter[s2[r]] = counter.get(s2[r], 0) + 1

        # one last check
        if counter == target:
                return True
        return False