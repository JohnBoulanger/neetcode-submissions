class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;
        while (l < r) {
            while(l < s.size() && !std::isalnum(std::tolower(s[l])) ) l++;
            while(r >= 0 && !std::isalnum(std::tolower(s[r]))) r--;
            if (l < s.size() && r >= 0 && l < r && std::tolower(s[l++]) != std::tolower(s[r--])) return false;
        }
        return true;
    }
};
