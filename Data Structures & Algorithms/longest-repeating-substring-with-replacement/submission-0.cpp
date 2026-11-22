class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0; int n = s.size();
        int result = 0;
        std::unordered_map<char, int> mp;
        for (int i = 0; i < 26; i++) {
            mp[(int)'A' + i] = 0;
        }

        for (int r = 0; r < n; r++) {
            // get most freq char in window
            int best = 0;
            char mostFreq = 'A';
            mp[s[r]]++;
            for (int i = 0; i < 26; i++) {
                char c = 'A' + i;
                if (mp[c] > best) {
                    best = mp[c];
                    mostFreq = c;
                }
            }
            int windowLen = r - l + 1;
            if (windowLen - mp[mostFreq] > k) {
                mp[s[l]]--;
                l++;
            }
            result = std::max(result, r - l + 1);
        }
        return result;
    }
};
