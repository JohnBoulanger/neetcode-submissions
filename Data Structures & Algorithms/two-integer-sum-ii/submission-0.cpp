class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        std::vector<int> res(2, 0);
        int l = 0;
        int r = n - 1;

        while (l < r) {
            if (numbers[r] + numbers[l] < target) l++;
            else if (numbers[r] + numbers[l] > target) r--;
            else if (numbers[r] + numbers[l] == target) {
                break;
            };
        }
        res[0] = l + 1;
        res[1] = r + 1;
        return res;
    }
};
