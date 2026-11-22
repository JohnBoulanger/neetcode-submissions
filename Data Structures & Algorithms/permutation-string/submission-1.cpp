class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char, int> s1Map;
        int n1 = s1.size();
        int n2 = s2.size();
        int l = 0;
        if (n2 < n1) return false;
        // add the first n1 elements into s1Map and track frequencies
        for (int i = 0; i < n1; i++) {
            s1Map[s1[i]] = s1Map[s1[i]] + 1;
        }

        for (int r = n1 - 1; r < n2; r++) {
            int i = l;
            bool match = true;
            std::unordered_map<char, int> s2Map;
            // add the elements in the window into s1Map and track frequencies
            while (i <= r) {
                s2Map[s2[i]] = s2Map[s2[i]] + 1;
                i++;
            }
            // check if maps are equal for the given window
            for (const auto& [key, value] : s1Map) {
                if (!match) break;
                auto it = s2Map.find(key);
                if (it == s2Map.end() || it->second != value) {
                    match = false;
                }
            }
            if (match == true) return true;
            l++;
        }
        return false;
    }
};
