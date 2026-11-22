class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maximum = 0;
        for (const auto &x : piles) {
            maximum = std::max(maximum, x);
        }

        int rate = maximum;
        int time = 0;
        int l = 1;
        int r = maximum;
        int bestRate = rate;
        while (l <= r) {
            time = 0;
            for (int i = 0; i < piles.size(); i++) {
                int x = piles[i];
                time += std::ceil(static_cast<double>(x) / rate);
            }
            // success, test with lower rate
            if (time <= h) {
                bestRate = rate;
                r = rate - 1;
                rate = (r + l) / 2;
            // fail, search with higher rate
            } else {
                l = rate + 1;
                rate = (r + l) / 2;
            }
        }
        return bestRate;
   }
};
