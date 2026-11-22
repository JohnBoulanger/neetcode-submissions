class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // backtracking solution
        vector<vector<int>> res;
        vector<int> subset;
        dfs(0, subset, res, nums);
        return res;
    }

    void dfs(int i, vector<int>& subset, vector<vector<int>>& res, vector<int>& nums) {
        // iterated through all combos, add the subset we got to the list of solutions
        if(i >= nums.size()) {
            res.push_back(subset);
            return;
        }
        // case where we do add the element nums[i]
        subset.push_back(nums[i]);
        dfs(i + 1, subset, res, nums);
        subset.pop_back();
        // case where we dont add the element nums[i]
        dfs(i + 1, subset, res, nums);
        return;
    }
};
