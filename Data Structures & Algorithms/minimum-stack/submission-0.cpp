class MinStack {
private:
    stack<int> st;
    stack<int> minSt;
    int minimum;
public:
    MinStack() {
        minimum = INT_MAX;
    };
    
    void push(int val) {
        st.push(val);
        minSt.push(std::min(val, minimum));
        if (val < minimum)
            minimum = val;
    }
    
    void pop() {
        st.pop();
        minSt.pop();
        if (minSt.empty()) {
            minimum = INT_MAX;
        } else {
            minimum = minSt.top();
        }
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return minSt.top();
    }
};
