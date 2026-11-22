class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        int result = 0;

        // number needed, current length
        unordered_map<int, int> hash;
        
        // turn the array into a hash table
        // give every value to each key 1 to start
        for (int i = 0; i < n; i++) {
            hash[nums[i]] = 1;
        }

        for (int i = 0; i < n; i++) {
            // start of a potential sequence
            if(hash.find(nums[i] - 1) == hash.end()) {
                // find sequence length
                int j = 1;
                while(hash.find(nums[i] + j) != hash.end()) {
                    j++;
                }
                result = max(result, j);
            }
        }
        return result;
    }
};
