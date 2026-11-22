class Solution {
public:
    int characterReplacement(string s, int k) {
        std::unordered_map<char, int> freqMap;
        int l = 0; int n = s.size();
        int result = 0;

        for (int r = 0; r < n; r++) {
            freqMap[s[r]] = freqMap[s[r]] + 1;
            // get most frequent char in freqMap
            int maximum = 0;
            for (auto &v : freqMap) {
                if (v.second > maximum) {
                    maximum = v.second;
                }
            }
            int windowLength = r - l + 1;
            while (windowLength - maximum > k) {
                if (freqMap[s[l]] >= 1) {
                    freqMap[s[l]] = freqMap[s[l]] - 1;
                } else {
                    freqMap.erase(s[l]);
                }
                l++;
                windowLength = r - l + 1;
            }

            result = std::max(result, r - l + 1);
        }
        return result;
    }
};
