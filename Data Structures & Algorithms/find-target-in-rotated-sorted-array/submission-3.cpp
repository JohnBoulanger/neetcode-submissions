class Solution {
public:
    int search(vector<int>& nums, int target) {
        // find minimum first (deflection)
        int l = 0;
        int r = nums.size() - 1;
        int m = (l + r) / 2;
        while (l <= r) {
            // in sorted part, search left
            // r cant be mininum so we can search before it
            if (nums[l] < nums[r]) {
                r = m - 1;
                m = (r + l) / 2;
            // minimum is in between l and r, search right
            } else if (nums[l] > nums[r]) {
                if (nums[m] > nums[r]) {
                    l = m + 1;
                } else {
                    r = m;
                }
                m = (r + l) / 2;
            } else {
                break;
            }
        }
        
        // m holds index of min, search right of it first
        int min = m;
        l = m;
        r = nums.size() - 1;
        while (l <= r){
            if (nums[m] < target) {
                l = m + 1;
                m = (r + l) / 2;
            } else if (nums[m] > target) {
                r = m - 1;
                m = (r + l) / 2;
            } else if (nums[m] == target) {
                return m;
            }
        }

        // search left if we fail
        r = min;
        l = 0;
        m = (l + r) / 2;
        while (l <= r) {
            if (nums[m] < target) {
                l = m + 1;
                m = (r + l) / 2;
            } else if (nums[m] > target) {
                r = m - 1;
                m = (r + l) / 2;
            } else if (nums[m] == target) {
                return m;
            }
        }
        return -1;
    }
};
