class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int tr = 0;
        int br = rows - 1;
        int mr = (tr + br) / 2;

        while (tr <= br) {
            // in a smaller row
            if (matrix[mr][0] > target && matrix[mr][cols - 1] > target) {
                br = mr - 1;
                mr = (tr + br) / 2;
            // in a larger row
            } else if (matrix[mr][0] < target && matrix[mr][cols - 1] < target) {
                tr = mr + 1;
                mr = (tr + br) / 2;
            } else {
                break;
            }
        }
        // potential target row found in mr
        int l = 0;
        int r = cols - 1;
        int m = (l + r) / 2;
        while (l <= r) {
            // further left
            if (matrix[mr][m] > target) {
                r = m - 1;
                m = (l + r) / 2;
            // further right
            } else if (matrix[mr][m] < target) {
                l = m + 1;
                m = (l + r) / 2;
            } else {
                return true;
            }
        }
        return false;
    }
};
