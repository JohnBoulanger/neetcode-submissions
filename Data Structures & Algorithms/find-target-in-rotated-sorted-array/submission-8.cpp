class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0; int r = nums.size() - 1; int n = nums.size();
        int mid = (l + r) / 2;
        // find the minimum and the binary search the left and right sides
        while (l < r) {
            // window between midpoint and r is unsorted, search right of midpoint
            if (nums[mid] > nums[r]) {
                l = mid + 1;
            }
            // window between midpoint and r is sorted, search left of and including midpoint
            else {
                r = mid;
            }
            mid = (l + r) / 2;
        }
        // l holds the minimum index
        int pivot = l;
        int result = 0;
        result = binarySearch(pivot, n, nums, target);
        if (result == -1) {
            return binarySearch(0, pivot, nums, target);
        }
        return result;
    }

    int binarySearch(int l, int r, vector<int>& nums, int target) {
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] < target) {
                l = mid + 1;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
};
