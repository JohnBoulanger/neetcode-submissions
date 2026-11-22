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
    bool isValidBST(TreeNode* root) {
        // keep track of maxAncestor and minAncestor ancestor at each part of the dfs
        // if we are checking a left node, it must be less than its parent but greater than the nearest left ancestor
        // checking a right node, greater than parent, less than nearest right ancestor
        return dfs(root, LONG_MIN, LONG_MAX);
    }

    bool dfs(TreeNode* root, long minAncestor, long maxAncestor) {
        if (!root) return true;
        if (root->val <= minAncestor || root->val >= maxAncestor) {
            return false;
        }
        return dfs(root->left, minAncestor, root->val) && dfs(root->right, root->val, maxAncestor);
    }
};
