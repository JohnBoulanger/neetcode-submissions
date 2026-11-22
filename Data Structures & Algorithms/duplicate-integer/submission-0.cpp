class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> h;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (h.find(nums[i]) != h.end()) return true;
            h.insert({nums[i], i});
        }
        return false;
    }
};