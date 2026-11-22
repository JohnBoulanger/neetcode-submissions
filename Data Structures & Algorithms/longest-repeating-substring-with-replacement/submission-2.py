class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        counts = {}
        for r in range(len(s)):
            # update counter
            counts[s[r]] = counts.get(s[r], 0) + 1

            # the window is invalid if the windows length - the most repeated characters amount 
            # is greater than k because there are more than k additional items in the window
            # shrink the window until its valid again
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            # update window when valid
            longest = max(longest, (r - l + 1))


        return longest


        