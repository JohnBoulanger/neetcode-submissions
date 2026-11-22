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
    int kthSmallest(TreeNode* root, int k) {
        // do a bfs, if a node is leaf, add it to the result,
        // otherwise add it to the res after we have completed the left search
        std::vector<int> res;
        dfs(root, res);
        return res[k-1];
    }

    void dfs(TreeNode* root, std::vector<int>& res) {
        if (!root) return;

        // check smaller nodes first
        dfs(root->left, res);
        // add self to res
        res.push_back(root->val);
        // check right nodes
        dfs(root->right, res);
        return;
    }
};
