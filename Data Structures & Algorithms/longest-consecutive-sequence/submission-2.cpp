class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> s(nums.begin(), nums.end());
        int n = s.size();

        int result = 0;
        for (int num : s) {
            if (s.find(num - 1) == s.end()) {
                int current = 0;
                while(s.count(num + current)) {
                    current++;
                }
                result = std::max(current, result);
            }
        }
        return result;
    }
};
