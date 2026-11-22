class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> res;
        int combos = pow(2, n);
        for (int i = 0; i < combos; i++) {
            vector<int> pass;
            // use the binary representation of i
            // any bit 1 means add to array, any bit 0 means dont add
            int copy = i;
            for (int j = 0; j < n; j++) {
                if (copy & 0x1 == 1) {
                    pass.push_back(nums[j]);
                }
                copy = copy >> 1;
            }
            res.push_back(pass);
        }
        return res;
    }
};
