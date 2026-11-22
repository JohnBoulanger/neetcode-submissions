class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0; int r = 0; int n = prices.size();
        int profit = 0;
        while (r < n) {
            if (prices[l] < prices[r]){
                profit = std::max(profit, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return profit;
    }
};
