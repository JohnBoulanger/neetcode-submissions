class Solution {
public:
    int findMin(vector<int> &nums) {
        int n = nums.size();
        int cur = nums[0];
        int prev;
        int l = 0;
        int r = n - 1;
        int i = 0;
        string direction = "right";

        if (cur < nums[(i + 1) % n] && cur < nums[i == 0 ? (n - 1) : i - 1]) {
            return cur;
        }

        prev = cur;
        i = ((l + 1) + r) / 2;
        cur = nums[i];
        
        while (cur > nums[(i + 1) % n] || cur > nums[i == 0 ? (n - 1) : i - 1]) {
            // increased when moving right, go right
            if (direction == "right" && cur > prev) {
                l = i + 1;
            }
            // decreased while moving right, go left
            else if (direction == "right" && cur < prev) {
                direction = "left";
                r = i - 1;

            } // increased when moving left, go right
            else if (direction == "left" && cur > prev) {
                direction = "right";
                l = i + 1;

            } // decreased when moving left, go left
            else if (direction == "left" && cur < prev) {
                r = i - 1;
            }
            prev = cur;
            i = (r + l) / 2;
            cur = nums[i];
        }
        return cur;
    }
};
