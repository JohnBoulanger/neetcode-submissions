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
        int minAncestor = -9999;
        int maxAncestor = 9999;
        bool res = true;
        dfs(root, minAncestor, maxAncestor, res);
        return res;
    }

    void dfs(TreeNode* root, int minAncestor, int maxAncestor, bool& res) {
        if (!root) return;
        if (root->val <= minAncestor || root->val >= maxAncestor) {
            res = res && false;
        }
        dfs(root->left, minAncestor, root->val, res);
        dfs(root->right, root->val, maxAncestor, res);
        return;
    }
};
