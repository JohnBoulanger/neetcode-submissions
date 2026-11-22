class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        std::unordered_map<int, int> ht;
        std::vector<int> result;
        for(int i = 0; i < n; i++) {
            if (ht.find(nums[i]) != ht.end()) {
                // found match return indicies pair
                int j = ht[nums[i]];
                if (i != j) {
                    result.push_back(j);
                    result.push_back(i);
                    return result;
                }
            }
            ht.insert({target - nums[i], i});
        }
        return result;
    }
};
