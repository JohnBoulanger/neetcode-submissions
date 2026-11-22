class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0; int n = s.length();
        if (n == 0) return 0;
        // (char, index)
        std::unordered_set<char> hset;
        int result = 0;
        for (int r = 0; r < n; r++) {
            // s[r] exists in map remove its first duplicate and any letters between
            // move l = the index of the duplicate in the set + 1
            while (hset.find(s[r]) != hset.end()) {
               hset.erase(s[l]);
               l++;
            }
            hset.insert(s[r]);
            result = std::max(result, r - l + 1);
        }
        return result;
    }
};
