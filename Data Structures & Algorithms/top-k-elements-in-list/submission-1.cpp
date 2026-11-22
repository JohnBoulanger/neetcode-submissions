class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> number_freq;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
           number_freq[nums[i]]++;
        }

        std::vector<std::vector<int>> freq_buckets(n + 1);
        
        // iterate over map and highest frequencies stored in largest index buckets
        for (const auto& entry : number_freq) {
            freq_buckets[entry.second].push_back(entry.first);
        }
        
        int total = 0;
        int i = n;
        std::vector<int> result;
        while (total < k) {
            for (int j = 0; j < freq_buckets[i].size() && total < k; j++) {
                result.push_back(freq_buckets[i][j]);
                total++;
            }
            i--;
        }
        return result;
    }
};
