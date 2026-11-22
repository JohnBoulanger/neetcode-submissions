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
        // for all nodes, maximum of max depth left + max depth right = total diameter
        if (!root) return 0;
        int result = 0;
        // do a dfs on the root, pass global result result
        dfs(root, result);
        return result;
    }

    int dfs(TreeNode* root, int& result) {
        if (!root) return 0;
        int left = dfs(root->left, result);
        int right = dfs(root->right, result);
        // store global best left + right height for every given node
        result = max(result, left + right);
        // leaf nodes return 1
        return 1 + max(left, right);

    }
};
