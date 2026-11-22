/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        // bfs, store rightmost node for every layer
        // pattern repeats even first is rightmost, odd last is rightmost
        int depth = 0;
        std::queue<TreeNode*> q;
        std::vector<int> res;
        if (!root) return res;
        
        // bfs
        q.push(root);
        while(!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* cur = q.front();
                q.pop();
                if (i == size - 1) {
                    res.push_back(cur->val);
                } 
                if (cur->left) {
                    q.push(cur->left);
                }
                if (cur->right) {
                    q.push(cur->right);
                }
            }
            depth++;
        }
        return res;
    }
};
