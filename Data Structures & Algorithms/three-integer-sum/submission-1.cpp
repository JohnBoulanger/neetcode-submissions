class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                int res = nums[i] + nums[l] + nums[r];
                if (res > 0){
                    r--;
                } 
                else if (res < 0){
                    l++;
                }
                else {
                    result.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while (nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }
        }
        return result;
    }
};
