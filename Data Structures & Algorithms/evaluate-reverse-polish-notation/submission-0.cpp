class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> st;
        int n = tokens.size();

        for (int i = 0; i < n; i++) {
            std::string val = tokens[i];
            if (val == "+" || val == "-" || val == "*" || val == "/") {
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();
                if (val == "+") {
                    st.push(b + a);
                } else if (val == "-") {
                    st.push(b - a);
                } else if (val == "*") {
                    st.push(b * a);
                } else if (val == "/") {
                    st.push(b / a);
                }
            } else {
                st.push(std::stoi(val));
            }
        }
        return st.top();
    }
};
