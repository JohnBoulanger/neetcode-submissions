class Solution {
public:


    string encode(vector<string>& strs) {
        int n = strs.size();
        string res;
        for (int i = 0; i < n; i++) {
            res += std::to_string(strs[i].length());
            res += "#";
            res += strs[i];
        }
        return res;
    }

    vector<string> decode(string s) {
        std::vector<string> res;
        int n = s.length();

        for (int ptr = 0; ptr < n; ) {
            int len = 0;
            string str_len;

            // find length of string
            while(ptr < n && s[ptr] != '#') {
                str_len += s[ptr++];
            }

            // convert string to number for length of decoded string
            len = std::stoi(str_len);

            // store the string in the array
            ptr++;
            len += ptr;
            string str_i;
            while(ptr < n && ptr < len) {
                str_i += s[ptr++];
            }
            res.push_back(str_i);
        }
        return res;
    }
};
