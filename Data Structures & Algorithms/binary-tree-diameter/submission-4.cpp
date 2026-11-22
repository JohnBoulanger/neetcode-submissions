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

    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        // global diameter value
        int result = 0;
        dfs(root, result);
        return result;
    }

    int dfs(TreeNode* root, int& result) {
        if (!root) return 0;
        // do dfs on node and get heights of l and r subtrees
        int left = dfs(root->left, result);
        int right = dfs(root->right, result);
        // update global diameter for this node
        result = std::max(result, left + right);
        // parent is one more height than deepest left or right subtree height
        return 1 + std::max(left, right);
    }
};
