#include <array>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        struct ArrayHash {
            size_t operator()(const array<int,26>& a) const {
                size_t h = 0;
                for (int x : a) h = h * 31 + x;
                return h;
            }
        };

        std::vector<std::vector<string>> solution;
        int n = strs.size();
        std::unordered_map<std::array<int,26>, std::vector<int>, ArrayHash> ht;
        std::vector<std::array<int,26>> char_map;

        // calculate histograms for each string and save it in char_map
        for (int i = 0; i < n; i++) {
            int l = strs[i].size();
            std::array<int,26> char_map_i{};
            for (int j = 0; j < l; j++) {
                char_map_i[(int)strs[i][j] - (int)'a']++;
            }
            char_map.push_back(char_map_i);
        }

        // add histograms to hash table and store index in strs in the vector
        for (int i = 0; i < n; i++) {
            ht[char_map[i]].push_back(i);
        }

        // iterate over hash table to build the solution
        int iter = 0;
        for (const std::pair<std::array<int,26>, std::vector<int>>& entry : ht) {
            const std::vector<int> val = entry.second;
            solution.push_back({});
            for (int i = 0; i < val.size(); i++) {
                solution[iter].push_back(strs[val[i]]);
            }
            iter++;
        }
    return solution;
    }
};