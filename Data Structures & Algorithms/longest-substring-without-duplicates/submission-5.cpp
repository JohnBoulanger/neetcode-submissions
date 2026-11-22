class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> charSet;
        int l = 0; int n = s.size();
        int result = 0;

        for (int r = 0; r < n; r++) {
            // duplicate character found
            if (charSet.find(s[r]) != charSet.end()) {
                while (charSet.find(s[r]) != charSet.end()) {
                    charSet.erase(s[l]);
                    l++;
                }
            }
            charSet.insert(s[r]);
            result = std::max(result, r - l + 1);
        }
        return result;
    }
};
