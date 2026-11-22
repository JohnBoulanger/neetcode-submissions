class Solution {
public:
    bool isAnagram(string s, string t) {
        if(t.length() != s.length()) return false;
        int n = t.length();
        std::vector<int> s_char_map(26);
        std::vector<int> t_char_map(26);
        // 26 spots for each possible character
        
        // iterate over s
        for (int i = 0; i < n; i++){
            s_char_map[(int)s[i] - (int)'a']++;
            t_char_map[(int)t[i] - (int)'a']++;
        }
        for (int i = 0; i < 26; i++){
            if (s_char_map[i] != t_char_map[i]) return false;
        }
        return true;
    }
};