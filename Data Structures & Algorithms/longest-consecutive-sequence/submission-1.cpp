class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        int result = 0;

        // number needed, current length
        unordered_set<int> hash(nums.begin(), nums.end());

        for (int num : hash) {
            // start of a potential sequence
            if(hash.find(num - 1) == hash.end()) {
                // find sequence length
                int j = 1;
                while(hash.find(num + j) != hash.end()) {
                    j++;
                }
                result = max(result, j);
            }
        }
        return result;
    }
};
