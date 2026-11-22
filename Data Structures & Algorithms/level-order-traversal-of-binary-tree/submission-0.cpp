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
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::queue<TreeNode*> q;
        int depth = 0;
        std::vector<std::vector<int>> res;
        if (!root) return res;

        // bfs
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            std::vector<int> layer;
            for (int i = 0; i < size; i++) {
                TreeNode *cur = q.front();
                q.pop();
                layer.push_back(cur->val);
                if (cur->left) {
                    q.push(cur->left);
                }
                if (cur->right) {
                    q.push(cur->right);
                }
            }
            depth++;
            res.push_back(layer);
        }
        return res;
    }
};
