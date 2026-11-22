class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> combination;
        dfs(nums, 0, target, combination, res);
        return res;
    }

    void dfs(vector<int> &nums, int i, int target,
             vector<int> combination, vector<vector<int>>& res) {

        // base case
        if (i >= nums.size()) return;
        if (nums[i] == target) {
            combination.push_back(nums[i]);
            res.push_back(combination);
            return;
        // overshot, return as array is sorted
        } else if (nums[i] > target) {
            return;
        }
        // skip current and go next
        dfs(nums, i + 1, target, combination, res);
        // add current to combo and stay
        combination.push_back(nums[i]);
        dfs(nums, i, target - nums[i], combination, res);
        return;
    }
};
