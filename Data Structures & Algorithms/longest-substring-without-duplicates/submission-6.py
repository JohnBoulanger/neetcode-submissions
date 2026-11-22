class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        longest = 0
        l = 0
        # sliding window, if a duplicate is found, close the window until the duplicate it matched
        # is removed, then add the "duplicate" back to the set and continue expanding window again
        # until another duplicate is found
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
            