class Solution {
public:
    int search(vector<int>& nums, int target) {
        // find minimum first (deflection)
        int l = 0;
        int r = nums.size() - 1;
        int m = (l + r) / 2;
                while (l < r) {
            int m = (l + r) / 2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        int pivot = l;
        r = nums.size() - 1;
        m = (r + l) / 2;
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
        r = pivot - 1;
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
