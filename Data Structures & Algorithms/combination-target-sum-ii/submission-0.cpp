class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> combination;
        dfs(candidates, 0, target, combination, res);
        return res;
    }

    void dfs(vector<int>& candidates, int i, int target,
             vector<int> combination, vector<vector<int>>& res) {

        if (i > candidates.size()) return;
        if (target == 0) {
            res.push_back(combination);
            return;
        } else if (target < 0) {
            return;
        }
        // add, go next
        combination.push_back(candidates[i]);
        int j = i;
        dfs(candidates, i + 1, target - candidates[i], combination, res);
                // skip duplicates
        while (j < candidates.size() && candidates[j] == candidates[j + 1]) {
            j++;
        }
        i = j;
        // dont add, go next not incl duplicates
        combination.pop_back();
        dfs(candidates, i + 1, target, combination, res);
        return;
    }
};
