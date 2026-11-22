class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        std::vector res(n, 0);
        std::stack<std::pair<int, int>> prev_temps;

        for (int i = 0; i < n; i++) {
            int cur_temp = temperatures[i];
            while(!prev_temps.empty() && prev_temps.top().first < cur_temp) {
                int gap = i - prev_temps.top().second;
                res[prev_temps.top().second] = gap;
                prev_temps.pop();
            }
            prev_temps.push(std::pair(cur_temp, i));
        }
        return res;
    }
};
