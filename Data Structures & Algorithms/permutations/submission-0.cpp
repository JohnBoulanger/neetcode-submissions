class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> taken(nums.size(), 0);
        vector<vector<int>> res;
        vector<int> permutation;
        dfs(nums, permutation, taken, res);
        return res;
    }
    void dfs(vector<int>& nums, vector<int>& permutation, vector<int>& taken, vector<vector<int>>& res) {
        if (permutation.size() == nums.size()) {
            res.push_back(permutation);
            return;
        }
        // add to permutation
        for (int i = 0; i < nums.size(); i++) {
            if (!taken[i]) {
                permutation.push_back(nums[i]);
                taken[i] = 1;
                dfs(nums, permutation, taken, res);
                permutation.pop_back();
                taken[i] = 0;
            }        
        }
    }
};
