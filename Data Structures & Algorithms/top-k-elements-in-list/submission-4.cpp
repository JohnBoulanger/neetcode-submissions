class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        std::unordered_map<int, int> frequencies;
        std::vector<int> res;

        // create a map that stores key: nums[i]
        // and value: number of times the value nums[i] appears in nums
        for (int i = 0; i < n; i++) {
            if (frequencies.find(nums[i]) != frequencies.end()) {
                frequencies[nums[i]]++;
            } else {
                frequencies.insert({nums[i], 1});
            }
        }

        std::vector<std::vector<int>> bucket(n+1);
        for (auto &v : frequencies) {
            bucket[v.second].push_back(v.first);
        }
        
        int counter = 0;
        for (int i = n; i >= 0 && counter < k; i--) {
            if (bucket[i].size() != 0) {
                int j = bucket[i].size() - 1;
                while (j >= 0 && counter < k) {
                    res.push_back(bucket[i][j]);
                    j--; counter++;
                }
            }
        }
        return res;
    }
};
