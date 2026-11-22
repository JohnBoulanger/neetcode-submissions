class Solution {
public:
    int search(vector<int>& nums, int target) {
        int r = nums.size() - 1;
        int l = 0;
        int mid = (r + l) / 2;
        while (l <= r) {
            if (nums[mid] < target) {
                l = mid + 1;
                mid = (r + l) / 2;
            } else if (nums[mid] > target) {
                r = mid - 1;
                mid = (r + l) / 2;
            } else {
                return mid;
            }
        }
        return -1;
    }
};
